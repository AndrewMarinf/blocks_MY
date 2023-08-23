# тут просто вызывем декортаор для раза все!
def repeater(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper
