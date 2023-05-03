lst = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
print(lst)
print(f"Максимум: {max(lst)}, минимум: {min(lst)}, сумма: {sum(lst)}")
print(f"Максимум: {max(lst, key = abs)}, минимум: {min(lst, key = abs)}, сумма: {sum(lst)}")

a = [1, 2, 3, 4, 5]
print(a)
print(a.index(4))