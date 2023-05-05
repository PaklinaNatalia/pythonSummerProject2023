sent = input("Введите предложение: ")
splitted_sent = sent.split()
for i in range(len(splitted_sent)):
    print(splitted_sent[i], len(splitted_sent[i]))
longest_word = ""
for j in splitted_sent:
    if len(j) > len(longest_word):
        longest_word = j
print(f"Самое длинное слово: {longest_word}")