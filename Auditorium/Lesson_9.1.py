dct ={1:123, 2:"234", 3:{1:111, 2:222}, 4:{1:"abc",2:"def"}}
x = 1
for k, v in dct.items():
    if k == x:
        print(v, end = " ")
    if type(v) == dict:
        for p, q in v.items():
            if p == x:
                print(q, end = " ")