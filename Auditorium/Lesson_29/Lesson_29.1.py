class Plates:
    def __init__(self):
        self.plt = []
    def put(self, plt_id):
        self.plt.append(plt_id)
    def get(self):
        if self.plt:
            return self.plt.pop()
        else:
            print("В стопке нет тарелок!")
    def how_many(self):
        return len(self.plt)
    def __str__(self):
        return str(self.plt)
p = Plates()
p.put(1)
p.put(2)
p.put(3)
print(p)
x = p.get()
print(x)
print(p)