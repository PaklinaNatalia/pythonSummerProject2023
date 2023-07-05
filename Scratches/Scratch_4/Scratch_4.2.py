class SomeClass1():
    attr1 = 42
    def __getattr__(self, attr):
        return attr.upper()
class SomeClass2():
    def __getattribute__(self, attr):
        return attr.upper()

o1 = SomeClass1()
print(f"{o1.attr1}\n{o1.attr2}")
print()
o2 = SomeClass2()
print(f"{o2.attr1}\n{o2.attr2}")

class SomeClass:
    attr1 = 44
    def __setattr__(self, name, value):
        print(name, value)
        self.__dict__[name] = value
        print(self.__dict__)

obj = SomeClass()
print(obj.attr1)
obj.attr1 = 123
obj.age = 100

#В переменной x содержится имя класса, а класс содержится в f1
x = input("Введите x: ")
f1 = type(x, (), {"f2": True})
obj = f1()
print(obj)