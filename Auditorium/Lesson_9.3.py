f = open ("../Texts/test_01.txt", "r", encoding ="utf-8") #открыть файл на чтение
s = f.readlines()
for i in s:
    if i.strip():
        print(i.strip())
f.close() #закрыть файл
print()

f = open ("../Texts/test_01.txt", "r", encoding ="utf-8")
for i in f:
    print(i.strip())
f.close()
print()