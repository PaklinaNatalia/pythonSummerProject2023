from time import time
number = 15000
my_list = list(range(number))
my_tuple = tuple(range(number))
my_set = set(range(number))
t = time()
for i in range(number):
    if i in my_list:
        pass
print(f"Операция со списком:{time() - t} секунд")
t = time()
for j in range(number):
    if j in my_tuple:
        pass
print(f"Операция с кортежем:{time() - t} секунд")
t = time()
for k in range(number):
    if k in my_set:
        pass
print(f"Операция с множеством:{time() - t} секунд")