def deco(func):
    def wrapper(*args, **kwargs):
        res = []
        for i in args:
            if type(i) == str:
                res.append(i)
        for i in kwargs.values():
            if type(i) == str:
                res.append(i)
        func(*args, **kwargs)
        return res
    return wrapper

@deco
def fu (*args, **kwargs):
    return

print(fu("a", "b", 1, [2, 3], first = 1, second = 2))