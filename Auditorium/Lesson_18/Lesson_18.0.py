class Figure:
    def __init__(self, perimeter, color = "Прозрачный"):
        self.color = color
        self.perimeter = perimeter

    def get_perimeter(self):
        print(self.perimeter)

    def set_perimeter(self, new_perimeter):
        self.perimeter = new_perimeter
        self.get_perimeter()

class Triangle(Figure):
    def __init__(self, a, b, c, color = "Прозрачный"):
        self.a = a
        self.b = b
        self.c = c
        self.color = color
        self.perimeter = 0

    def t_info(self):
        print(f"a = {self.a}\nb = {self.b}\nc = {self.c}\nПериметр = {self.perimeter}")

    def set_perimeter(self):
        self.perimeter = self.a + self.b + self.c
        self.t_info()
        return self.perimeter

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.perimeter = 0

    def set_perimeter(self):
        self.perimeter = 2 * (self.a + self.b)
        self.r_info()
        return self.perimeter

    def r_info(self):
        print(f"a = {self.a}\nb = {self.b}\nПериметр = {self.perimeter}")

t = Triangle(5, 5, 5)
t.set_perimeter()
r = Rectangle(2, 4)
r.set_perimeter()