f = open ("../../Texts/text_04.txt", "r", encoding ="utf-8")
s = f.read()
f.close()

g = open ("../../Texts/text_02.txt", "w", encoding ="utf-8")
for i in s[::2]:
    g.write(i)
    print(i, end = "")
g.close()