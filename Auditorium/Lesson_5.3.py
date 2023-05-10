d = {}
while True:
    s = (input("Товар: "))
    if s == "0":
        print("Ввод окончен")
        break
    z = s.split()
    d[z[0]] = d.get(z[0], 0) + int(z[1])
for i in sorted(d):
    print(i, d[i])