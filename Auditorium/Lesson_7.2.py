def uni_let(lst):
    tes = set()
    for i in lst:
        for j in i:
            tes.add(j)
    sorted_tes = sorted(tes)
    res1 = "".join(sorted_tes)
    return res1, len(res1)
print(uni_let([]))
print(uni_let(["definition"]))
print(uni_let(["definition", "solution"]))