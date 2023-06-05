import re

def rename(x):
    s = x.group()
    print(x.group(), x.start(), x.end())
    if s == "LED":
        return "Пулково"
    elif s == "MSQ":
        return "Минск"
    elif s == "SVO":
        return "Шереметьево"
    elif s == "SVX":
        return "Кольцово"
    else:
        return s

text = "LED ABC MSQ SVO SVX"
print(re.sub(r"\b\w{3}\b", rename, text))