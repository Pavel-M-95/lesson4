from functools import reduce
def my_func(el, el_1):
    return el * el_1
print('Результат умножения четных чисел:')
print(reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0]))





