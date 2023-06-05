dct = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11}, 6:22}

def rec_dict(d, x):
    lst = []
    for k, v in d.items():
        if k == x:
            lst.append(v)
        if type(v) == dict:
            lst.extend(rec_dict(v, x))
    return lst

print(rec_dict(dct, int(input("Введите значение ключа: "))))