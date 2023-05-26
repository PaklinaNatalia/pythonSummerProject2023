def FizzBuzz(x):
    return "FizzBuzz" if x%15 == 0 else "Fizz" if x%3 == 0 else "Buzz" if x%5 == 0 else x

s = [FizzBuzz(i) for i in range(1, 21)]
print(*s)