s = input("Введите слова: ").split()
tes = set()
for i in s:
    tes = tes | set(i)
    print(f"{i = } {set(i) = } {tes = }")
print(len(tes))