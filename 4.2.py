# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55] статичный список
# Заправшиваем числа у пользователя
# a = input('Введите числа через пробел: ')
my_list = [int(i) for i in input('Введите числа через пробел: ').split(' ')]
new_list = [el for id, el in enumerate(my_list) if my_list[id - 1] < my_list[id] and id != 0]
print(my_list)
print(new_list)

