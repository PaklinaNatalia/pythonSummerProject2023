f = open ("../Texts/test_03.txt", "r", encoding ="utf-8")
s = f.readlines()
f.close()
g = open ("../Texts/test_04.txt", "w", encoding ="utf-8")
for i in s:
    if not set(i) & set("0123456789"):
        g.write(i)
        print(i)
g.close()