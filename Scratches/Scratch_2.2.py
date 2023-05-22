d = {"G":"C", "C":"G", "T":"A", "A":"T"}
dna = input("Введите цепочку ДНК: ")
rna = ""
for i in dna:
    rna += d.get(i, "*")
print(rna)

dct = {1:{11:{111:1111}}, 2:{22:{222:2222}}, 3:{33:333}, 4:44}
for k, v in dct.items():
    print(k, ":", v)
    if type(v) == dict:
        for p, q in v.items():
            print(p, ":", q)
            if type(q) == dict:
                for x, y in q.items():
                    print(x, ":", y)