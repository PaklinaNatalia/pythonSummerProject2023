n_num = int(input("Введите число: "))
n_str = str(n_num)
for i in range(0, 10):
      i_str = str(i)
      print(f"{i_str} – {n_str.count(i_str)}")