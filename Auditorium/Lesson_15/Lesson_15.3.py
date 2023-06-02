s = [1, "2", [11, "22", [111, "222", [1111, "2222", 3333, "4444"], 333, "444"], 33, "44"], 3, "4"]
r = []
p = []
def rec_list(z):
    for i in z:
        if type(i) == list:
            rec_list(i)
        elif type(i) == int:
            r.append(i)
        elif type(i) == str:
            p.append(i)

rec_list(s)
print(r)
print(p)