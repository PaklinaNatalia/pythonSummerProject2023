class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @age.setter
    def age(self, age):
        if age < 0 or age > 20:
            raise ValueError("Возраст указан неверно.")
        else:
            self.__age = age

    @name.setter
    def name(self, name):
        if name != name.title():
            raise ValueError("Возраст указан неверно.")
        else:
            self.__name = name

    @age.deleter
    def age(self):
        del self.__age

    @name.deleter
    def name(self):
        del self._name

c = Cat("Белка", -1)
print(c.age)