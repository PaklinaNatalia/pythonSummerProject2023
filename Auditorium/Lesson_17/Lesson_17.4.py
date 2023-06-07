class Pet:
    def __init__(self, name, weight, satiety):
        self.name = name
        self.weight = weight
        self.satiety = satiety

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Вес: {self.weight}")
        print(f"Уровень сытости: {self.satiety}")

    def hungry(self):
        self.info()
        if self.satiety <= 25:
            print("Питомец голоден!")
        else:
            print("Питомец сыт!")

    def feed(self, food):
        while self.satiety < 100:
            self.satiety += food
        self.info()

a = Pet("Snow", 2.5, 25)
a.hungry()
a.feed(5)
a.hungry()