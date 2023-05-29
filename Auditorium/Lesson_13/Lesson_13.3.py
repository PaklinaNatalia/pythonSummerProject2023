def sum_lst(lst):
    i = 0
    while True:
        i += 1
        yield (sum(lst[:i]))

lst = list(map(int, input("Введите список: ").split()))
gen_sum = sum_lst(lst)
for _ in range(len(lst)):
    print(next(gen_sum))