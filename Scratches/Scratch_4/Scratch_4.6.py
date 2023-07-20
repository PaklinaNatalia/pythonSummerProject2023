from collections import Counter
def extra_number(lst):
    c = Counter(lst)
    for k, v in c.items():
        if v == 1:
            return k
print(extra_number(map(int, input("Введите числа: ").split())))