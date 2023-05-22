import collections
f = open ("../Texts/text_01.txt", "r", encoding ="utf-8")
s0 = f.read()
s0 = s0.lower()
s0 = sorted(dict(collections.Counter(s0)).items(), key = lambda x: (-x[1], x[0]))
for i, j in s0[:10]:
    print(i, "–", j)
f.close()