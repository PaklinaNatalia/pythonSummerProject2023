class Student:
    student_list = []
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
        Student.student_list.append(self)
    def money(self):
        return self.fives*5+self.tens*10+self.twenties*20
    def __lt__(self, other):
        return self.money() < other.money()

s1 = Student("Alice", 0, 0, 0)
s2 = Student("Rose", 20, 10, 5)
s3 = Student("Jason", 5, 10, 20)
s4 = Student("Gabriel", 1, 2, 3)
for i in Student.student_list:
    print(i.name, i.money())
print()
for i in sorted(Student.student_list):
    print(f"{i.name}:{i.money()}")
print()
print(f"Минимум: {min(Student.student_list).name}")
print(f"Максимум: {max(Student.student_list).name}")