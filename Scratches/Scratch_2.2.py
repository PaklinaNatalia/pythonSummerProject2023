d = {"G":"C", "C":"G", "T":"A", "A":"T"}
dna = input("Введите цепочку ДНК: ")
rna = ""
for i in dna:
    rna += d.get(i, "*")
print(rna)