#Крайне странный принцип работы
s = input("Введите слово: ")
def mask(x):
    res = []
    for i, j in enumerate(x):
        if j in "ауоыиэяюёе":
            res.append(i)
    return(res)
print(mask(s))
out = []
z = input("Введите слова для сравнения: ").split()
for i in z:
    if mask(i) == mask(s):
        out.append(i)
print(*out)