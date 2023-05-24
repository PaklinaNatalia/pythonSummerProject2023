t = input("Введите слово: ")
g, s = [], []
for i in t:
    if i in "aeiou":
        g.append(i)
    else:
        s.append(i)
if abs(len(g) - len(s)) > 1:
    print("Impossible!")
else:
    if len(g) > len(s): s, g = g, s
    res = ""
    for i in range(len(g)):
        res += s[i]
        res += g[i]
    if len(s) > len(g):
        res += s[-1]
    print(res)