#Печать квадратов
f = open ("../Texts/text_02.txt", "w", encoding ="utf-8")
for i in range(1, 10):
    print(f"{i}x2 = {i**2}", file = f)
f.close()
f = open ("../Texts/text_02.txt", "r", encoding ="utf-8")
for i in f:
    print(i.strip())
f.close()