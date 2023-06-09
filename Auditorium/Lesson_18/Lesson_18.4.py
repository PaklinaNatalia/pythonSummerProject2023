class Data:
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]

class Teacher:
    def __init__(self):
        self.work = 0

    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1

class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)

lesson = Data("Math", "English", "Art", "Sociology", "History")
jason = Teacher()
kendra = Pupil()
rose = Pupil()

jason.teach(lesson[2], kendra, rose)
jason.teach(lesson[0], rose)
jason.teach(lesson[1], kendra)

print(kendra.knowledge)
print(rose.knowledge)
print(jason.work)