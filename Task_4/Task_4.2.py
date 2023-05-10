n = int(input("Введите число: "))
spiral = [[0] * n]
for a in range(n - 1):
    spiral += [[0] * n]
dx, dy, x, y = 0, 1, 0, 0
for i in range(1, n ** 2 + 1):
    spiral[x][y] = i
    if spiral[(x + dx) % n][(y + dy) % n]:
        dx, dy = dy, -dx
    x += dx
    y += dy
for b in spiral:
	print(*(f"{c :< 4}" for c in b), sep = "")