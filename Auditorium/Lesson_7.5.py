#Четность-нечетность чисел [0; n]
#ЕСЛИ четное, ТО печатаем n[i]^2
#ЕСЛИ нечетное, ТО печатаем n[i]^3
def check(i):
    def chet(i):
        print(i, "Четное")
        return i ** 2
    def nechet(i):
        print(i, "Нечетное")
        return i ** 3
    if i % 2:
        res = nechet(i)
    else:
        res = chet(i)
    return res

n = int(input("Введите число: "))
for i in range(n + 1):
    print(check(i))