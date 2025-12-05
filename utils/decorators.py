from functools import wraps

def log_extra_args(func):
    """
    A decorator to handle extra keyword arguments.
    """
    @wraps(func)
    def wrapper(self, msg, *args, **kwargs):
        extra_info = kwargs
        return func (self, msg, *args, extra = extra_info)
    return wrapper

def log_action(level="debug"):
    """
    Decorator to automatically log method calls.

    Works stricly with a Logger-class object.
    
    :param level: Logging level as string: "debug", "info", "warning", "error", "critical"
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            getattr(self.logger, level)(f"{func.__name__} called with args={args}, kwargs={kwargs}")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator
