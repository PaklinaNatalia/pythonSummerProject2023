s = list(map(int, input("Введите числа: ").split()))
lst = []
for i in range(len(s)-1):
    if s[i] != s[i+1]-1:
        lst.append(s[i+1])
if len(lst) == 0:
    print(f"В списке {s} нет непоследовательных чисел.")
else:
    print(f"Исходная последовательность: {s}\nРезультат: {lst}")