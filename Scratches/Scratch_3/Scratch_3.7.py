import math

class Shape:
    #Инициализация объекта
    def __init__(self, color, square, type):
        self.color = color
        self.square = square
        self.type = type

    #Сводная информация о фигуре
    def info_shape(self):
        print("-" * 30)
        print(f"Цвет фигуры: {self.color}")
        print(f"Площадь фигуры: {self.square} ед. изм.²")
        print(f"Тип фигуры: {self.type}")
        print("-" * 30)

    #Установить цвет фигуры
    def set_color(self):
        shape_color = str(input("Введите цвет: "))
        self.color = shape_color

    def set_type(self):
        print("Выберите тип фигуры:\n0 – круг\n1 – треугольник\n2 – квадрат\n3 – прямоугольник\n4 – ромб")
        x = int(input("Введите число: "))
        if x == 0:
            self.type = "Круг"
        elif x == 1:
            self.type = "Треугольник"
        elif x == 2:
            self.type = "Квадрат"
        elif x == 3:
            self.type = "Прямоугольник"
        elif x == 4:
            self.type = "Ромб"
        else:
            print("Неизвестная фигура!")

    def set_square(self):
        if self.type == "Круг":
            r = float(input("Введите радиус: "))
            if r <= 0:
                print("Ошибка! Радиус должен быть положительным числом.")
            else:
                self.square = round(math.pi * r ** 2, 4)
        elif self.type == "Треугольник":
            a = float(input("Введите сторону 1: "))
            b = float(input("Введите сторону 2: "))
            c = float(input("Введите сторону 3: "))
            if a <= 0 or b <= 0 or c <= 0:
                print("Ошибка! Сторона должна быть положительным числом.")
            else:
                p = (a+b+c)/2
                self.square = round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 4)
        elif self.type == "Квадрат":
            a = float(input("Введите сторону: "))
            if a <= 0:
                print("Ошибка! Сторона должна быть положительным числом.")
            else:
                self.square = round(a**2, 4)
        elif self.type == "Прямоугольник":
            a = float(input("Введите сторону 1: "))
            b = float(input("Введите сторону 2: "))
            if a <= 0:
                print("Ошибка! Сторона должна быть положительным числом.")
            elif a == b:
                print("Ошибка! Несоотвествие сторон типу фигуры.")
            else:
                self.square = a * b
        elif self.type == "Ромб":
            a = float(input("Введите сторону: "))
            h = float(input("Введите высоту: "))
            if a <= 0 or h <= 0:
                print("Ошибка! Сторона/высота должна быть положительным числом.")
            else:
                self.square = round(a * h, 4)
        else:
            self.square = int(input("Введите площадь фигуры: "))

s = Shape("Прозрачный", 0, "Произвольный")
s.info_shape()
s.set_color()
s.set_type()
s.set_square()
s.info_shape()

