class Plus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Plus(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"Plus ({self.x}, {self.y})"

a = Plus(1, 2)
b = Plus(10, 20)
print (a+b)