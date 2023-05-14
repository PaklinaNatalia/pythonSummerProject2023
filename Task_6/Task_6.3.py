alphabet = sorted(set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))
numbers = sorted(set("1234567890"))
t = set(map(str, input("Введите строку: ")))
a = set()
n = set()
s = set()
for i in t:
    if i in alphabet:
        a.add(i)
    elif i in numbers:
        n.add(i)
    else:
        s.add(i)
if len(a) != 0:
    print(*sorted(a))
if len(n) != 0:
    print(*sorted(n))
if len(s) != 0:
    print(*sorted(s))
