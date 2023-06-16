import itertools
for i in itertools.chain([1, 2, 3], "abcdef", (11, 22, "abc"), {1:11, 22:222}.values()):
    print(i)

import itertools
def odd_num(x):
    return x%2
s = [1, 2, 4, 6, 3, 3, 10, 8, 4]
for k, v in itertools.groupby(s, key = odd_num):
    print(k, "–", *v)