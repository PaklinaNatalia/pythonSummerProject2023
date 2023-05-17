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