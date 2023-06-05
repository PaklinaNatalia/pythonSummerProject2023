def sample_deco(func):
    def wrapper():
        result = func()
        new_result = result.upper()
        return new_result
    return wrapper

@sample_deco
def say():
    return "Hello"

@sample_deco
def talk():
    return "Goodbye"

print(say())
print(talk())
print(say() + talk())
print(say() + " " + talk())