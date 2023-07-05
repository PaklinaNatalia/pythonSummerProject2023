def darth(n):
    for i in range(n):
        for j in range(n):
            print(min(i, j, n-i-1, n-j-1) + 1, end = " ")
        print()
print(darth(int(input("Введите n: "))))