import rubxy
import asyncio

from rubxy import handlers

class AddHandler:
    def add_handler(
        self: "rubxy.Client",
        handler: "handlers.Handler",
        group: int = 0
    ):
        if isinstance(handler, handlers.StartHandler):
            self.start_handlers.append(handler.callback)
        
        elif isinstance(handler, handlers.StopHandler):
            self.stop_handlers.append(handler.callback)
            
        else:
            self.loop.create_task(self.dispatcher.add_handler(handler, group))