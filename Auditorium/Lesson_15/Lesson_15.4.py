import re

string = "Косой Костя косой косил траву на косе в покос и был ужален осой"
regex = r"\b\w*[Кк]ос\w*\b"
print(re.findall(regex, string))