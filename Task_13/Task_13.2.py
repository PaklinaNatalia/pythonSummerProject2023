#Ряд числовых палиндромов
def palindrome(start = 1, stop = 300, step = 1):
   for i in range(start, stop, step):
       if str(i) == str(i)[::-1]:
           yield i

print(*palindrome())