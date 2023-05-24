#Количество вхождений каждого символа слова в слово
s = input("Введите строку: ")
dct = {}
for k in s:
    if k not in dct:
        dct[k] = 0
    dct[k] += 1
print(dct)
s = input("Введите число: ")

# s = input("Введите число: ")
# dct = {}
# for k in s:
#     dct[k] = dct.get(k, 0) + 1
# print(dct)