class Figure:
    def __init__(self, perimeter, square, color, type):
        self.perimeter = perimeter
        self.square = square
        self.color = color
        self.type = type

    def info(self):
        print(f"Периметр: {self.perimeter}\nПлощадь: {self.square}\nЦвет: {self.color}\nТип фигуры: {self.type}")

    def set_perimeter(self):
        self.perimeter = float(input("Введите периметр: "))

    def set_square(self):
        self.square = float(input("Введите площадь: "))

    def set_color(self):
        self.color = input("Введите цвет: ")

f = Figure(0, 0, "Прозрачный", "Произвольная")
f.info()
f.set_perimeter()
f.set_square()
f.set_color()
f.info()