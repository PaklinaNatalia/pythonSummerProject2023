def tri_asterisk(n):
    if n == 0:
        return
    else:
        #print("*" * n)
        tri_asterisk(n - 1)
        print("*" * n)

tri_asterisk(int(input("Введите n: ")))