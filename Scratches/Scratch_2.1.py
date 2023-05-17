t = [(1, 2), (0, 2), (1, 1), (0, 0), (0, 1), (1, 0)]
def fu1(p):
    return -p[0], -p[1]
def fu2(p):
    return -p[0], p[1]
print(sorted (t, key = fu1))
print(sorted (t, key = fu2))
print()

print("aaa bbb ccc ddd".title())
print("ааа ббб ввв ггг".title())
print()

lst = [222, 21, 1, 111, 12, 322]
print(sorted(lst, key = lambda x: (x % 10, x)))
print()

lst = [111, 22, 12, 21, 33, 5, 6, 66, 3]
print(sorted(lst, key = lambda x: (x % 2, x)))
print(sorted(lst, key = lambda x: (x % 2, x % 10, x)))
print()

lst = [111, 22, 12, 21, 33, 5, 6, 66, 3]
print(sorted(lst, key = lambda x: (x % 2, -x)))
print(sorted(lst, key = lambda x: (x % 2, x % 10, -x)))
print()

lst = input("Введите строку: ").split()
print(sorted(lst, key = lambda x: x.lower()))
print(sorted(lst, key = lambda x: x.upper()))
print()

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x % 2 == 0, numbers)))
print(list(filter(lambda x: x % 2, numbers)))
print(list(filter(lambda x: x % 3 == 0, numbers)))
print(list(map(lambda x: x % 2 == 0, numbers)))
print(list(map(lambda x: x % 2, numbers)))
print(list(map(lambda x: x % 3 == 0, numbers)))
print()

numbers = [123, 234, 345, 456, 567, 678, 789, 890, 901]
print(list(map(lambda x: sum(map(int, str(x))), numbers)))