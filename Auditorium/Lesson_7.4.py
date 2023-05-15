#Четность-нечетность чисел [0; n]
def check(i):
    def chet(i):
        print(i, "Четное")
    def nechet(i):
        print(i, "Нечетное")
    if i % 2:
        nechet(i)
    else:
        chet(i)

n = int(input("Введите число: "))
for i in range(n + 1):
    check(i)