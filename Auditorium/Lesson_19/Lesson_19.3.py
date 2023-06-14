class Fact:
    def __init__(self, limit):
        self.value = 1
        self.index = 1
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        self.value *= self.index
        self.index += 1
        if self.index > self.limit + 1:
            raise StopIteration
        return f"{self.index-1}: {self.value}"
f = Fact(int(input("Введите число: ")))
for i in f:
    print(i)