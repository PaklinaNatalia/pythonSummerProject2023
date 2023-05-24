s = input("Введите строку: ").split()
dct = {}
res = ""
for k in s:
    dct[k] = dct.get(k, 0) + 1
    #print(k, "_", dct[k], sep = "", end = " ")
    res += k + "_" + str(dct[k]) + " "
print(res.strip())