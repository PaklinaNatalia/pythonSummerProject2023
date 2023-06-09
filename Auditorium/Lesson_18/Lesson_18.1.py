class Student:
    group = []

    def __init__(self, name):
        self.name = name
        Student.group.append(self.name)

    def show(self):
        print(f"Hello, {self.name}!")

    def __del__(self):
        print(self.name)

s = Student("Jason")
s.show()
s = Student("Gabriel")
s.show()