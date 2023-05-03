#Варианты форматирования
n = 123
s = "abc"
print(f"{n}___{s}")
print(f"{n:4}___{s}")
print(f"{n:4}___{s:5}")
print(f"{n:4}___{s:>5}")
print(f"{n:<4}___{s:>5}")
print(f"{n:0<4}___{s:*>5}")
print(f"{n:04}___{s:*<5}")