def double_it(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper * 2