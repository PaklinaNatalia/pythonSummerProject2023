f = open ("../Texts/test_05.txt", "r", encoding ="utf-8")
s = f.read()
f.close()

g = open ("../Texts/test_06.txt", "w", encoding ="utf-8")
for i in s[::2]:
    g.write(i)
    print(i, end = "")
g.close()