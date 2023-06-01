def validate(name):
    if len(name) < 10:
        raise ValueError

try:
    name = input("Введите имя: ")
    validate(name)
except ValueError:
    print("Слишком короткое имя!")