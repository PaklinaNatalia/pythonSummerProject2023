class Sums:
    def __init__(self, limit):
        self.value = 0
        self.index = 1
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        self.value += self.index
        if self.index > self.limit:
            raise StopIteration
        self.index += 1
        return self.value
s = Sums(int(input("Введите число: ")))
for i in s:
    print(i)