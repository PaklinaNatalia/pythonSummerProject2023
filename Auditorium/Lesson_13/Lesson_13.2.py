def factorial():
    f, k = 1, 1
    while True:
        print(f"{k = } {f = }")
        yield f
        k += 1
        f *= k

gf = factorial()
for i in gf:
    print(f"{i = }")
    input("Нажмите любую клавишу...")