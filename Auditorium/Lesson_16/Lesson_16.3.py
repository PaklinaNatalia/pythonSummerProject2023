def reverse(func):
    def wrapper():
        result = func()
        new_result = " ".join(result.split()[::-1])
        return new_result
    return wrapper

@reverse
def say():
    return "Hello ladies and gentlemens"

@reverse
def talk():
    return "Goodbye ladies and gentlemens"

print(say())
print(talk())