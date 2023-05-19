#Генетический код (A – аденин, G – гуанин, C – цитозин, T – тимин)
s0 = input("Введите цепочку ДНК: ")
print(s0)
s1 = ""
i = 0
while True:
    if s0[i:i+2] == "AG":
        s1 += "GA"
        i += 2
    elif s0[i:i+2] == "GA":
        s1 += "AG"
        i += 2
    elif s0[i:i+2] == "CT":
        s1 += "CAGT"
        i += 2
    elif s0[i:i+2] == "TC":
        s1 += "TGAC"
        i += 2
    else:
        s1 += s0[i]
        i += 1
    if i >= len(s0) - 1:
        break
print(s1)