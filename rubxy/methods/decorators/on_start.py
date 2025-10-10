import rubxy

from rubxy import handlers

class OnStart:
    def on_start(self: "rubxy.Client"):
        def decorator(func):
            self.add_handler(handlers.StartHandler(func))
            
            return func
        return decorator