input_list = [10, 'э', 15, 'ABC', 1]
for i in input_list:
    if type(i) == str:
        print(i * 5)
    elif type(i) == int:
        print(i ** 2)
    else:
        print(i)