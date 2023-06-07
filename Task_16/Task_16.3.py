def deco(func):
    def wrapper(text):
        res = func(text)
        return res.title()
    return wrapper
@deco
def s(text):
    return(text)

print(s(input("Введите строку: ")))