def max_palindrome(s):
    lens = len(s)
    for i in range(lens, -1, -1):
        for j in range(lens - i):
            ds = s[j:i+j+1]
            print(ds)
            if ds == ds[::-1]:
                return ds
s = input("Введите строку: ")
print(max_palindrome(s))