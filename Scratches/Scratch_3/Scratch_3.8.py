class SomeClass():
    def __init__(self):
        self.__param = 42
    def get_param(self):
        return self.__param
obj = SomeClass()
print(obj._SomeClass__param, obj.get_param())

class Person:
    instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance
    def __init__(self):
        self.__name = "Jason"
p1 = Person()
p2 = Person()
print(p1 is p2)

class Test():
    def __init__(self, *args, **kwargs):
        self.x = 0
        self.y = 1
    def __str__(self):
        return ", ".join(str(i)+":"+str(j) for i, j in self.__dict__.items())
obj = Test(0, 1)
print(obj)

class Car:
    def __init__(self, model, color, vin):
        self.model = model
        self.color = color
        self.vin = vin
    def __eq__(self, other):
        #return self.vin == other.vin
        #return self.model == other.model and self.vin == other.vin
        return self.model == other.model and self.color == other.color and self.vin == other.vin
car_1 = Car("Mercedes", "silver", "N0000001")
car_2 = Car("Mercedes", "black", "N0000001")
print(car_1 == car_2)

class IntNum:
    def __init__(self, number):
        self.number = number
    def __eq__(self, other):
        return self.number == other.number
a = IntNum(-3)
b = IntNum(-3)
print(a == b)

class LineGen:
    def __init__(self, k, b):
        self.k = k
        self.b = b
    def __call__(self, x):
        return self.k * x + self.b
lf_1 = LineGen(2, 5)
lf_2 = LineGen(-6, 9)
print(f"{lf_1(10)}\n{lf_2(4)}")

class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration
    def __iter__(self):
        return self
s_iter = SimpleIterator(4)
for i in s_iter:
    print(i)

import itertools
s = "aabb"
res = set()
for i in itertools.permutations(s):
    res.add("".join(i))
print(*res)