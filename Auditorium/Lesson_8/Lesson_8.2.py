#Генетический код (А – аденин, Г – гуанин, Ц – цитозин, Т – тимин)
s = "АААГЦТАГЦТАГЦТТТ"
def often(s, n):
    d = {}
    for i in range(len(s)):
        d[s[i:i+n]] = d.get(s[i:i+n], 0) + 1
    m = max(d.values())
    res = []
    for k, v in d.items():
        if v == m:
            res.append(k)
    return m, res, res[0]
print(*often(s, 3))