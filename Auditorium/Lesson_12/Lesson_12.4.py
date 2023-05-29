lst = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
dct = {str(k):v for k,v in enumerate(lst)}
print(dct)
n = int(input("Введите число: "))
st = [dct[i] for i in str(n)]
print(" ".join(st))