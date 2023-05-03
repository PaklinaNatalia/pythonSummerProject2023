#Проверка строки на палиндромность
s = input()
n = len(s)
for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        print(False)
        break
    else:
        print(True)