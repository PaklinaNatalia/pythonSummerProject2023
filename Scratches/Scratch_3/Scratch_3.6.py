import re
def fullname(x):
    s = x.group()
    print(x.group(), x.start(), x.end())
    if s == "Наташа":
        return "Наталья"
    else:
        return s
text = "Привет, Наташа!"
print(re.sub(r"\b\w{6}\b", fullname, text))

import re
text = "first second"
print(re.sub(r"(first)(second)", r"\2 \1", text))

import re
text = "Паклина Наталья Сергеевна"
print(re.sub(r"(\w+) (\w+) (\w+)", r"\2 \3 \1", text))

import re
text = "Фамилия фамилия Фамилия"
print(re.sub(r"Фамилия", "Паклина", text, count = 2))
print(re.sub(r"Фамилия", "Паклина", text, count = 2, flags = re.I))

import re
text = "123:first 234:second"
print(re.findall(r"(\d+):(\w+)", text))

import re
text = "www.a.com www.bb.com www.ccc.info www.dddd.by"
print(re.findall(r"www.(\w+).(?:ru|com|by)", text))

import re
text = "abracadabra"
res1 = re.finditer(r"a", text)
for i in res1:
    print(i.group(), i.start(), i.end())
print()
res2 = re.finditer(r"[^a]", text)
for i in res2:
    print(i.group(), i.start(), i.end())

import re
def f(x):
    return "A" + str(x.start())
text = "abracadabra"
print(re.sub(r"a", f, text))

import re
from collections import Counter
text = "длинношеее трон бесконечность кот рацион"
s = re.findall(r"\b\w+\b", text)
for i in s:
    if max(Counter(i).values()) > 1:
        print(i)

import re
num = re.compile(r"\d+")
print(re.findall(num, "aaa 111 dddd 123 c"))
print(num.findall("aaa 111 dddd 123 c"))

import re
x = 3
print(re.findall(fr"{x+x}", "11223344556677889900"))
print(re.findall(fr"{str(x)*2}", "11223344556677889900"))