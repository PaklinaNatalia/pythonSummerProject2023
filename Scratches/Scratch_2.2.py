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

from functools import reduce
sum = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
fact = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(sum, fact)

with open ("../Texts/text_02.txt", "w", encoding ="utf-8") as fout:
    for i in range(10):
        print(i, i**2, file = fout)
        print(111, i, i**2)
with open ("../Texts/text_02.txt", "r", encoding ="utf-8") as fin:
    for i in fin:
        print(222, i.strip())