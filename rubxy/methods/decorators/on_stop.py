import rubxy
import inspect

from rubxy import handlers

class OnStop:
    def on_stop(self: "rubxy.Client"):
        def decorator(func):
            self.add_handler(handlers.StopHandler(func))
            
            return func
        return decorator