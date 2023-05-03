lst = [[1, 2, 3], [10, 20], [100]]
s = 0
for i in lst:
    s += sum(i)
print(s)
lst = [[1, 2, 3], [10, 20], [100]]
s = 0
for i in lst:
    for j in i:
        s += j
print(s)