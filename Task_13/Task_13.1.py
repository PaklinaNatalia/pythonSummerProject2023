#Бесконечная последовательность вида 1, -2, 3, -4, 5, -6, ...
def infinity():
    n = 1
    while True:
    #Для тестирования while n != 10:
        yield n
        n += 1

for i in infinity():
    if i % 2 == 0:
        print(-i, end = " ")
    else:
        print(i, end=" ")