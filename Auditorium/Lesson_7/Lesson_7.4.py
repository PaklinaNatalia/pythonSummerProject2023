# Функция FizzBuzz
def fb(i):
    def fb_3(i):
       return "Fizz"
    def fb_5(i):
       return "Buzz"
    def fb_15(i):
       return "FizzBuzz"
    def fb_other(i):
        return str(i)
    if i % 15 == 0:
        res = fb_15(i)
    elif i % 3 == 0:
        res = fb_3(i)
    elif i % 5 == 0:
        res = fb_5(i)
    else:
        res = fb_other(i)
    return res
for i in range(int(input("Введите i: ")) + 1):
    print(fb(i))