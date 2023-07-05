def __init__(self, x, y):
    self.x = x
    self.y = y
Point = type("Point", (), {'__init__':__init__})
po = Point(1, 2)
def __str__(self):
    return f"{self.x}:{self.y}"
Point.__str__ = __str__

lst = [(0, 0), (1, 1), (2, 2), (0, 1)]
plst = [Point(xy[0], xy[1]) for xy in lst]
for i in range(len(plst)):
    for j in range(i + 1, len(plst)):
        k, l = plst[i], plst[j]
        length = (k.x - l.x) ** 2 + (k.y - l.y) ** 2
        if length > 1:
            print(k, l)