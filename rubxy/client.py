import logging
import warnings
import asyncio
import time
import inspect
import os
import sys

from aiohttp import ClientSession, ClientTimeout, TCPConnector
from concurrent.futures import ThreadPoolExecutor
from collections import deque

from rubxy import enums
from rubxy.methods import Methods
from rubxy.handlers import Handler
from rubxy.dispatcher import Dispatcher
from rubxy.parser import Markdown

from typing import Any, Union, Literal, Dict, List, Callable, Optional
from importlib import import_module
from pathlib import Path

from ._config import (
    DEAFULT_HOST,
    DEAFULT_PORT,
    DEAFULT_PATH,
    DEAFULT_TIMEOUT,
    DEAFULT_RATE_LIMIT,
    DEAFULT_POLL_INTERVAL
)

logger = logging.getLogger(__name__)

class Client(Methods):
    """
    Rubika Client, the main means for interacting with Rubika.

    ---

    **Parameters:**

    - `bot_token` (`str`): Pass the Bot API token to create a bot.
    - `plugins` (`dict`, optional): Smart Plugins settings as dict, e.g. `dict(root="plugins")`.
    - `timeout` (`float`, optional): Long polling wait time in seconds (default: 30).
    """

    def __init__(
        self,
        bot_token: str,
        plugins: Optional[dict] = None,
        timeout: Optional[float] = DEAFULT_TIMEOUT,
        rate_limit: Optional[float] = DEAFULT_RATE_LIMIT,
        poll_interval: Optional[float] = DEAFULT_POLL_INTERVAL,
        parse_mode: Optional[Union[str, enums.ParseMode]] = None,
        executor: Optional[ThreadPoolExecutor] = None,
        loop: Optional[asyncio.BaseEventLoop] = None
    ):
        self.bot_token: str = bot_token
        self.base_url: str = "https://botapi.rubika.ir/v3/{}/".format(bot_token)
        self.http: ClientSession = None
        self.connector: TCPConnector = None
        self._formatter = Markdown(self)
        self.is_started: bool = False
        self.is_long_polling: bool = None
        self.middlewares: List[Callable] = []
        self.dispatcher: Dispatcher = Dispatcher(self, poll_interval=poll_interval)
        self.plugins: dict = plugins
        self.timeout: int = timeout
        self.parse_mode = parse_mode
        self.completed_updates = deque(maxlen=200)
        self.rate_limit: float = rate_limit
        self.last_request = 0
        self.executor = executor or ThreadPoolExecutor(min(32, (os.cpu_count() or 1) + 4))
        self.loop = loop

        self.start_handlers: List[Callable] = []
        self.stop_handlers: List[Callable] = []
        
        if isinstance(loop, asyncio.AbstractEventLoop):
            self.loop = loop
        else:
            self.loop = asyncio.get_event_loop()

        # parse_mode normalizer

        if self.parse_mode is None:
            self.parse_mode = enums.ParseMode.MARKDOWN

        elif isinstance(self.parse_mode, str):
            if self.parse_mode.lower() in ("mk", "markdown"):
                self.parse_mode = enums.ParseMode.MARKDOWN
            elif self.parse_mode.lower() in ("html"):
                self.parse_mode = enums.ParseMode.HTML
            else:
                raise ValueError("parse_mode must be type of enums.ParseMode or in [html, mk, markdown]")
        
    async def start(self):
        if not self.is_started:
            self.is_started = True
            timeout = ClientTimeout(total=self.timeout)
            
            if self.connector is None:
                self.connector = TCPConnector(limit=50)
            
            if self.http is None:
                self.http = ClientSession(
                    base_url=self.base_url,
                    connector=self.connector,
                    timeout=timeout,
                )
        
        for handler in self.start_handlers:
            if inspect.iscoroutinefunction(handler):
                await handler(self)
            else:
                self.loop.run_in_executor(
                    self.executor,
                    handler,
                    self
                )
        
        return self
    
    async def stop(self):
        if self.is_started:
            self.is_started = False
            self.dispatcher.is_running = False

            for handler in self.stop_handlers:
                if inspect.iscoroutinefunction(handler):
                    await handler(self)
                else:
                    self.loop.run_in_executor(
                        self.executor,
                        handler,
                        self
                    )

    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

    async def __aenter__(self):
        await self.start()
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.stop()

    async def _rate_limit(self):
        passed = time.time() - self.last_request

        if passed < self.rate_limit:
            await asyncio.sleep(self.rate_limit - passed)
        
        self.last_request = time.time()

    def load_plugins(self):
        if not self.plugins:
            return
        
        plugins = self.plugins.copy()
        root = plugins.get("root")
        include = plugins.get("include", [])
        exclude = plugins.get("exclude", [])
        count = 0

        if not root or not isinstance(root, str):
            raise ValueError("`root` parameter is required for plugins")

        for path in sorted(Path(root.replace('.', '/')).rglob('*.py')):
            module_path = '.'.join(path.parent.parts + (path.stem,))
            logger.info("`%s` module loading...", module_path)
            module = import_module(module_path)

            for name in vars(module).keys():
                try:
                    for handler, group in getattr(module, name).handlers:
                        self.add_handler(handler, group)
                        count += 1
                except Exception:
                    pass
        
        logger.info("%s plugins are loaded successfuly", count)

    def run(
        self,
        endpoint: Optional[str] = None,
        host: Optional[str] = DEAFULT_HOST,
        path: Optional[str] = DEAFULT_PATH,
        port: Optional[int] = DEAFULT_PORT,
        update_endpoints: Optional[bool] = True
    ) -> None:
        self.load_plugins()

        runner = self.loop.run_until_complete
        runner(self.start())

        if endpoint:
            if endpoint.startswith('http'):
                runner(self.dispatcher.setup_webhook(host=host, path=path, port=port, endpoint=endpoint, update_endpoints=update_endpoints))

                try:
                    self.loop.run_forever()
                except KeyboardInterrupt as e:
                    runner(self.stop())
                    raise e
                finally:
                    runner(self.dispatcher.app.shutdown())
                    runner(self.dispatcher.app.cleanup())
            else:
                raise ValueError("Endpoint format is incorrect, it should be starts with http")
        else:
            warnings.warn(
                "Note: long-polling cannot receive `InlineMessage` updates",
                UserWarning
            )

            self.is_long_polling = True

            try:
                runner(self.dispatcher.updater(limit=100))
            except KeyboardInterrupt as e:
                runner(self.stop())
                raise e