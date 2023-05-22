dna = input("Введите цепочку ДНК: ")
rna = ""
i = 0
while True:
    if dna[i:i + 1] == "G":
        rna += "C"
        i += 1
    elif dna[i:i + 1] == "C":
        rna += "G"
        i += 1
    elif dna[i:i + 1] == "T":
        rna += "A"
        i += 1
    elif dna[i:i + 1] == "A":
        rna += "T"
        i += 1
    else:
        rna += dna[i]
        i += 1
    if i >= len(dna):
        break
print(rna)