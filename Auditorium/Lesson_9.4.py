f = open ("../Texts/text_02.txt", "w", encoding ="utf-8") #открыть файл на запись
s = input("Напишите что-нибудь: ")
f.writelines(s)
f.close() #закрыть файл