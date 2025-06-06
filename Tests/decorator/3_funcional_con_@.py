def decorator_func(fn):
    def wrapper():
        return f"Decorated: {fn()}"
    return wrapper

@decorator_func
def say_hello():
    return "Hello"
