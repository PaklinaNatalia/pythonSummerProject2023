original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
p_list = [i for i in original_prices if i > 0]
print(*p_list)
n_list = [i for i in original_prices if i < 0]
print(*n_list)
print(sum(original_prices))
print(sum(p_list) + sum(n_list))
print(sum(p_list), sum(n_list), round(sum(original_prices), 2) == round(sum(p_list) + sum(n_list), 2))