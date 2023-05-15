#Всякие примерчики
a = [1, 2, 3, 'cat', True, False, [100, 101]]
b = a[:]
a[0] = 111
print(*a)
print(*b)
print()

a = [1, 2, 3, 4]
print(*a)
b = list('cat')
print(*b)
print()

mass = [1, 2, 3, 4]
print(len(mass))
print(len('cat'))
print()

a = [10, 20, 30, 40]
for k, v in enumerate(a):
    print(k, v)
print()

print(*list(range(10)))
print()

input_list = [10, 'э', 15, 'ABC', 1]
for i in input_list:
    if type(i) == str:
        print(i * 5)
    elif type(i) == int:
        print(i ** 2)
    else:
        print(i)
print()

a = [4, 'cat', 6, 3]
a.append(3)
print(*a)
print()

for i in range(ord("A"), ord("A") + 26):
    print(i, chr(i))
print()

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
print()

lst = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
print(lst)
print(f"Максимум: {max(lst)}, минимум: {min(lst)}, сумма: {sum(lst)}")
print(f"Максимум: {max(lst, key = abs)}, минимум: {min(lst, key = abs)}, сумма: {sum(lst)}")
print()

a = [1, 2, 3, 4, 5]
print(a)
print(a.index(4))
print()

def counter():
    num = 0
    def incr():
        nonlocal num
        num += 1
        print(num)
        return num
    print(num)
    x = incr()
    return x
inc = counter()
print(inc)
print()

def uni_let(lst):
    tes = set()
    for i in lst:
        for j in i:
            tes.add(j)
    sorted_tes = sorted(tes)
    res1 = "".join(sorted_tes)
    return res1, len(res1)
print(uni_let([]))
print(uni_let(["definition"]))
print(uni_let(["definition", "solution"]))