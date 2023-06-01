class Positive(ValueError):
    pass
class Negative(ValueError):
    pass

def f(lst):
    for i in lst:
        try:
            if i > 0:
                raise Positive("+")
            elif i < 0:
                raise Negative("–")
            else:
                print("0")
        except Positive as e:
            print(e)
        except Negative as e:
            print(e)
    return "Конец!"

print(f([-1, 0, 1]))