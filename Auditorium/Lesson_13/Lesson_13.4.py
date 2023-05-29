def numbers():
    i = 0
    while True:
        i += 1
        for j in range(i):
            yield i

gen_num = numbers()
for i in range(int(input("Введите число: "))):
    print(next(gen_num), end = " ")