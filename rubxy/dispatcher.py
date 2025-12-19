import rubxy
import asyncio
import logging
import inspect
import time

from rubxy import types, enums, handlers, errors
from collections import OrderedDict
from typing import Callable, Dict, List, Union
from asyncio import sleep
from aiohttp import web, ClientResponseError
from aiohttp.web import Application, Request

logger = logging.getLogger(__name__)

ALLOWED_IPS: list = []

class Dispatcher:
    def __init__(
        self,
        client: "rubxy.Client",
        poll_interval: float
    ):
        self.client = client
        self.application: Application = None 
        self.groups = {}
        self.last_offset = None
        self.poll_interval = poll_interval
        self.is_running = False
        self.is_first_update = True
        self.lock = asyncio.Lock()

    def has_time_passed(
        self,
        last_time,
        seconds
    ):
        try:
            timestamp = int(float(last_time))
            now = time.time()
            return (now - timestamp) > seconds
        except (TypeError, ValueError):
            return False
    
    async def add_handler(
        self,
        handler: "handlers.Handler",
        group: int = 0
    ):
        group = int(group)

        async with self.lock:
            event_type = handler.event_type
            
            if event_type not in self.groups:
                self.groups[event_type] = OrderedDict()

            if group not in self.groups[event_type]:
                self.groups[event_type][group] = []

            self.groups[event_type][group].append(handler)
            self.groups[event_type] = OrderedDict(sorted(self.groups[event_type].items()))
    
    async def updater(self, limit: int):
        self.is_running = True
        self.next_offset_id = None

        try:
            while self.is_running:
                try:
                    updates = await self.client.invoke(
                        "getUpdates",
                        offset_id=self.next_offset_id,
                        limit=limit
                    )
                    
                    if not all(
                        [
                            updates.get("updates"),
                            updates,
                        ]
                    ):
                        await sleep(self.poll_interval)
                        continue
                    
                    self.next_offset_id = updates.get("next_offset_id", self.next_offset_id)
                    updates = updates.get("updates", [])

                    if self.is_first_update:
                        updates = []
                        self.is_first_update = False
                        continue
                    
                    tasks: list = []

                    for raw_update in updates:
                        tasks.append(
                            self.process_update(
                                raw_update,
                                enums.EventType.INLINE_MESSAGE if 'inline_message' in raw_update else enums.EventType.MESSAGE
                            )
                        )
                    
                    if tasks:
                        await asyncio.gather(*tasks)
                
                except ClientResponseError:
                    if self.client.is_long_polling:
                        pass
                    
                except Exception:
                    logger.exception('an error occurred while polling update')
        except KeyboardInterrupt:
            await self.client.stop()

    async def process_update(self, raw_update: Union[Dict], event_type: enums.EventType):
        if not isinstance(raw_update, dict):
            raise TypeError("Updates type must be dict, not %s"%type(update).__name__)

        if event_type is enums.EventType.MESSAGE:
            raw_update = raw_update.get("update", raw_update) or {}
            new_message = raw_update.get("new_message") or {}
            aux_data = new_message.get("aux_data") or {}
            file = new_message.get("file") or {}
            forwarded_from = new_message.get("forwarded_from") or {}
            updated_message = raw_update.get("updated_message") or {}
            updated_payment = raw_update.get("updated_payment") or {}
            updated_message_aux_data = updated_message.get("aux_data") or {}
            updated_message_file = updated_message.get("file") or {}
            updated_message_forwarded_from = updated_message.get("forwarded_from") or {}
            update = types.Update(
                type=raw_update.get("type"),
                chat_id=raw_update.get("chat_id"),
                removed_message_id=raw_update.get("removed_message_id"),
                new_message=types.Message(
                    id=new_message.get("message_id"),
                    text=new_message.get("text"),
                    time=new_message.get("time"),
                    is_edited=new_message.get("is_edited"),
                    sender_type=new_message.get("sender_type"),
                    sender_id=new_message.get("sender_id"),
                    aux_data=types.AuxData(
                        start_id=aux_data.get("start_id"),
                        button_id=aux_data.get("button_id"),
                        client=self.client
                    ) if aux_data else None,
                    file=types.File(
                        file_id=file.get("file_id"),
                        file_name=file.get("file_name"),
                        size=file.get("size"),
                        client=self.client
                    ) if file else None,
                    reply_to_message_id=new_message.get("reply_to_message_id"),
                    forwarded_from=types.ForwardedFrom(
                        type_from=forwarded_from.get("type_from"),
                        id=forwarded_from.get("message_id"),
                        from_chat_id=forwarded_from.get("from_chat_id"),
                        from_sender_id=forwarded_from.get("from_sender_id"),
                        client=self.client
                    ) if forwarded_from else None,
                    metadata=new_message.get("metadata"),
                    client=self.client
                ) if new_message else None,
                updated_message=types.Message(
                    id=updated_message.get("message_id"),
                    text=updated_message.get("text"),
                    time=updated_message.get("time"),
                    is_edited=updated_message.get("is_edited"),
                    sender_type=updated_message.get("sender_type"),
                    sender_id=updated_message.get("sender_id"),
                    aux_data=types.AuxData(
                        start_id=updated_message_aux_data.get("start_id"),
                        button_id=updated_message_aux_data.get("button_id"),
                        client=self.client
                    ) if updated_message_aux_data else None,
                    file=types.File(
                        file_id=updated_message_file.get("file_id"),
                        file_name=updated_message_file.get("file_name"),
                        size=updated_message_file.get("size"),
                        client=self.client
                    ) if updated_message_file else None,
                    reply_to_message_id=updated_message.get("reply_to_message_id"),
                    forwarded_from=types.ForwardedFrom(
                        type_from=updated_message_forwarded_from.get("type_from"),
                        id=updated_message_forwarded_from.get("message_id"),
                        from_chat_id=updated_message_forwarded_from.get("from_chat_id"),
                        from_sender_id=updated_message_forwarded_from.get("from_sender_id"),
                        client=self.client
                    ) if updated_message_forwarded_from else None,
                    metadata=updated_message.get("metadata"),
                ) if updated_message else None,
                updated_payment=types.PaymentStatus(
                    payment_id=updated_payment.get("payment_id"),
                    status=updated_payment.get("status"),
                    client=self.client
                ) if updated_payment else None,
                client=self.client
            )
        elif event_type is enums.EventType.INLINE_MESSAGE:
            raw_update = raw_update.get("inline_message") or {}
            file = raw_update.get("file") or {}
            location = raw_update.get("location") or {}
            aux_data = raw_update.get("aux_data") or {}
            update = types.InlineMessage(
                sender_id=raw_update.get("sender_id"),
                text=raw_update.get("text"),
                file=types.File(
                    file_id=file.get("file_id"),
                    file_name=file.get("file_name"),
                    size=file.get("size"),
                    client=self.client
                ) if file else None,
                location=types.Location(
                    longitude=location.get("longitude"),
                    latitude=location.get("latitude"),
                    client=self.client
                ) if location else None,
                aux_data=types.AuxData(
                    start_id=aux_data.get("start_id"),
                    button_id=aux_data.get("button_id"),
                    client=self.client
                ) if aux_data else None,
                message_id=raw_update.get("message_id"),
                chat_id=raw_update.get("chat_id"),
                client=self.client
            )
        
        await self.dispatch_update(update=update, event_type=event_type)

    async def dispatch_update(self, update, event_type):
        async def run_middlewares(index: int):
            if index < len(self.client.middlewares):
                mw = self.client.middlewares[index]

                if inspect.iscoroutinefunction(mw):
                    await mw(self.client, update, lambda: run_middlewares(index + 1))
                else:
                    self.client.loop.run_in_executor(
                        self.client.executor,
                        mw,
                        self.client, update, lambda: self.client.loop.create_task(run_middlewares(index + 1))
                    )
            else:
                event_handlers: Dict[int, List[handlers.Handler]] = self.groups.get(event_type) or {}

                for group, _handlers in event_handlers.items():
                    for _handler in _handlers:
                        try:
                            _check = await _handler.check(self.client, update)

                            if _check:
                                break
                            
                        except rubxy.StopPropagation:
                            break
                        except rubxy.ContinuePropagation:
                            continue
        
        await run_middlewares(0)
    
    def handle_webhook(self, event_type: enums.EventType):
        async def handle(request: Request):
            raw_update = await request.json()
            
            asyncio.create_task(self.process_update(raw_update=raw_update, event_type=event_type))

            return web.json_response(
                {"status": "OK"},
                status=200
            )

        return handle
    
    def get_real_ip(self, request: Request):
        if 'X-Forwarded-For' in request.headers:
            return request.headers['X-Forwarded-For'].split(',')[0].strip()
        return request.remote
    
    @web.middleware
    async def ip_range_check(self, request: Request, handler: Callable):
        ip = self.get_real_ip(request)

        if ip not in ALLOWED_IPS:
            return web.json_response(
                {'error': 'Access denied'},
                status=403
            )
        
        return await handler(request)
    
    async def setup_webhook(self, host: str, path: str, port: int, endpoint: str, update_endpoints: bool):
        _path = path.rstrip('/')
        pather = lambda a=None, b=_path: f"{b}/{a}" if a else ""
        decapitalize = lambda s: s[:1].lower() + s[1:] if s else s
        handler = self.handle_webhook

        self.app = Application()
        self.app.router.add_post(pather(), handler(enums.EventType.MESSAGE))
        self.app.router.add_post(pather("receiveUpdate"), handler(enums.EventType.MESSAGE))
        self.app.router.add_post(pather("receiveInlineMessage"), handler(enums.EventType.INLINE_MESSAGE))

        if update_endpoints:
            for type in list(enums.UpdateEndpointType):
                _endpoint = endpoint.rstrip('/') + path
                
                result = await self.client.update_endpoints(
                    url=pather(
                        a=decapitalize(type),
                        b=_endpoint
                    ),
                    type=type
                )

                if result.get("status") != "Done":
                    raise errors.ApiError(status=result.get("status"))

                logger.info(
                    'Endpoint: %s | Type: %s | Status: %s',
                    _endpoint, type, result.get("status", "failure").lower()
                )

        runner = web.AppRunner(self.app)
        await runner.setup()

        site = web.TCPSite(runner, host=host, port=port)
        await site.start()