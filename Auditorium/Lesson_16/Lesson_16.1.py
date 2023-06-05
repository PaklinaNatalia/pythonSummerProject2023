import re

x = 5
text = "11223344556677889900"
res = "|".join(str(i) for i in range(x))
print(re.findall(fr"{res}", text))
print(res)