def hourglass_plus(n, d = 0):
    if n == 0:
        return
    elif n == 1:
        print(" " * d + "+")
    else:
        print(" " * d + "+ " * n)
        hourglass_plus(n - 1, d + 1)
        print(" " * d + "+ " * n)
hourglass_plus(int(input("Введите n: ")))

import re
string_1 = "567-678-789-890-901 999-034-2707 369-369-369 921-237-1586 123-234-345-456"
regex = r"\d{3}-\d{3}-\d{4}"
print(re.findall(regex, string_1))

string_2 = "P070TK178 А123ВС456"
regex = r"\b[A-ZА-Я]\d{3}[A-ZА-Я]{2}\d{2,3}"
print(re.findall(regex, string_2))

import re
string_1 = "Я изучаю Java."
regex_1 = r"Java"
regex_2 = r"Python"
string_2 = re.sub(regex_1, regex_2, string_1)
print(string_1, string_2)

import re
string = "(095) 095 ((095)) 1095 1(095)"
regex_1 = r"\(095\)"
regex_2 = r"(812)"
print(re.sub(regex_1, regex_2, string))

import re
string = "12 throne 444 9 cat 3 trinity 0 2 999 twilight 4 33 369 eternity 000 14 69 love 24 32"
regex_1 = r"\b\d*[02468]\b"
print(re.findall(regex_1, string))

import re
string = "12 throne -2 444 9 cat 333 trinity 0 525 999 twilight -003 4 112 55 369 eternity 000 15 69 love 005 24 30"
regex_1 = r"[+-]?\d+\b"
print(sum(list(map(int, re.findall(regex_1, string)))))