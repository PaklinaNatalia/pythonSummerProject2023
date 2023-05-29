s = [p.split("–") for p in input("Введите список: ").split(", ")]
r = [k for p in s for k in range(int(p[0]), int(p[1]) + 1)]
print(*s)
print(*r)