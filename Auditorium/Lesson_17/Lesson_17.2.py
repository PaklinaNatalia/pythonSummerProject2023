import time

def deco(func):
    def wrapper(*args, **kwargs):
        with open("../../Texts/log.txt", "a") as f:
            print(time.ctime(), func.__name__, "Start", file = f)
        try:
            func(*args, **kwargs)
        except Exception as e:
            with open("../../Texts/log.txt", "a") as f:
                print(time.ctime(), func.__name__, "Error!", e, file=f)
        with open("../../Texts/log.txt", "a") as f:
            print(time.ctime(), func.__name__, "Finish", file = f)
        return
    return wrapper

@deco
def sleep(n):
    time.sleep(n)

@deco
def test():
    print(1/0)

sleep(int(input("Введите время для сна: ")))
test()