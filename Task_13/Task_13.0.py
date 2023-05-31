def tribonacci(n):
    t1, t2, t3, t4 = -3, 1, 1, -1
    for _ in range(n):
        t1, t2, t3, t4 = t2, t3, t4, 2 * t4 - t1
        yield t4

print(*tribonacci(int(input("Введите количество элементов ряда: "))))