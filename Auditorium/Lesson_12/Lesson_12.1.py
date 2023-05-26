from string import ascii_letters

#QйwЦEуrКTеyН
s = input("Введите строку: ")
is_en = [print(f"{letter} – EN") if letter in ascii_letters else print(f"{letter} – RU") for letter in s]
print()
is_only_en = [print(f"{letter} – EN") for letter in s if letter in ascii_letters]
print()
is_only_ru = [print(f"{letter} – RU") for letter in s if letter not in ascii_letters]