#Использование глобальной переменной
s = 0
print("000", s)
def a():
    #global s
    s = 1
    print("111", s)
    def b():
        #global s
        s = 2
        print("222", s)
    b()
    print("333", s)
a()
print("444", s)
s = 3
print("555", s)