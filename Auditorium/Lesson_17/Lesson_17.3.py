class Person:
    def __init__(self, name, money, interest):
        self.name = name
        self.money = money
        self.interest = interest

    def give_money(self, other, x_money):
        if self.money < x_money:
            print("Не могу дать больше, чем есть!")
        else:
            other.money += x_money
            self.money -= x_money
            self.info()
            other.info()

    def equal_money(self, other):
        x = (self.money + other.money)//2
        self.money = x
        other.money = x
        self.info()
        other.info()

    def info(self):
        print(f"{self.name}: §{self.money}")

    def income(self, years):
        for i in range(1, years + 1):
            self.money = round(self.money * (1 + self.interest/100), 2)
            print(f"{i} год = {self.money}")

a = Person("Rose", 200, 5)
b = Person("Anna", 300, 7.5)

#a.give_money(b, 100) #b.give_money(a, 100)
#a.equal_money(b) #b.equal_money(a)
#a.income(10) # b.income(10)

class Teacher(Person):
    pass

c = Teacher("Jason", 1000, 9.5)
c.info()