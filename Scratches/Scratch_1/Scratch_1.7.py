def f(**kwargs):
    res = 1
    string = ""
    for k, v in kwargs.items():
        if type(v) == int:
            res *= v
        elif type(v) == str:
            string += v
    return res, string

print(f(id = 1, age = 29, name = "Natalia", surname = "Paklina"))

def many_all(var1, var2, *args, **kwargs):
    print(var1, var2)
    print(*args)
    print("a", "b", **kwargs)

print(many_all(10, 34, 77, sep = " ", end = "20"))