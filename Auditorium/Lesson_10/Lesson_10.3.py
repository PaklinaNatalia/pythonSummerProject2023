with open ("../../Texts/text_01.txt", "r", encoding ="utf-8") as fin:
    s = fin.readlines()
with open ("../../Texts/text_02.txt", "w", encoding ="utf-8") as fout:
    for i in s:
        x = " ".join(sorted(i.strip().split())) + "\n"
        print(x, file = fout)
with open ("../../Texts/text_02.txt", encoding ="utf-8") as fi:
    for i in fi:
        print(i)