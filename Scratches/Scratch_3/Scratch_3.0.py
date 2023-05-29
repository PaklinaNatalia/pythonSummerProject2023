import sys
a = [x for x in range(1000)]
print(type(a), len(a), sys.getsizeof(a))
print()
b = (x for x in range(1000))
print(type(b), sys.getsizeof(b))