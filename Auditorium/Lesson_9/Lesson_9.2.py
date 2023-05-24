import collections
x = "С помощью Counter определите, какая буква содержится больше всего в строке x"
a = collections.Counter(x)
b = dict(a)
print(sorted(b.items(), key = lambda x: -x[1])[:3])