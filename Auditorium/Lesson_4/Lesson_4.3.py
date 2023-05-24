#Наиболее часто встречающееся слова в тексте с пробелами
s = input("Введите текст: ").split()
d = {}
for i in s:
    if i not in d:
        d[i] = 0
    d[i] += 1
ma, ms = 0, ''
for k in d:
    if d[k] > ma:
        ma = d[k]
        ms = k
print(ms, ma)