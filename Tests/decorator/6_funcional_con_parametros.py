def decorator_with_args(prefix):
    def real_decorator(fn):
        def wrapper():
            return f"{prefix}: {fn()}"
        return wrapper
    return real_decorator

@decorator_with_args(">>>")
def greet():
    return "Hi"