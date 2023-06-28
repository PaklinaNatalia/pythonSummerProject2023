s = list(map(int, input("Введите числа: ").split()))
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] > s[j]:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
print(s)