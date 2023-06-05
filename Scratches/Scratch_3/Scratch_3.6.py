import re

def fullname(x):
    s = x.group()
    print(x.group(), x.start(), x.end())
    if s == "Наташа":
        return "Наталья"

text = "Здравствуй, Наташа!"
print(re.sub(r"\b\w{6}\b", fullname, text))