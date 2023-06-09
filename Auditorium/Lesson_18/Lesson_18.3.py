class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    def display(self):
        print(f"Имя: {self.name}\nВозраст: {self.__age}")

p = Person("Rose")
p.__age = 50
print(f"Возраст: {p.__age}")
p.display()
print(p.__dict__)