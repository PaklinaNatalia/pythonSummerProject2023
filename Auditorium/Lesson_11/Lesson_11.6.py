import time

def fsleep_2():
    t0 = time.time()
    time.sleep(2)
    t1 = time.time()
    return t1 - t0

def fsleep_3():
    t0 = time.time()
    time.sleep(3)
    t1 = time.time()
    return t1 - t0

sleep_2, sleep_3 = 0, 0
for i in range(11):
    if i % 2:
        sleep_3 += fsleep_3()
    else:
        sleep_2 += fsleep_2()
print (sleep_2, sleep_3)