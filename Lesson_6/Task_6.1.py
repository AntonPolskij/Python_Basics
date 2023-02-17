# 6.1[39]. Даны два списка чисел. Требуется вывести те элементы первого списка , которых нет во втором списке.

# Создайте функцию.

# Аргументы: два списка целых чисел

# Возвращает: список элементов (смотри условие)

# Примеры/Тесты:

# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [2, 3, 12]

# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3,4]

# [*] Усложнение. Элементы необходимо возвращать в том порядке, в котором они находятся в первом списке, с учетом повторений

# Примеры/Тесты:

# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [3, 3, 2, 12]

# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3, 4, 3, 4]
from time import perf_counter
from random import randint


def difference_set(lst1, lst2):
    t_1 = perf_counter()
    lst3 = list(set(lst1).difference(set(lst2)))
    t_2 = perf_counter()
    return lst3, t_2 - t_1


def difference_list(lst1, lst2):
    t_1 = perf_counter()
    list3 = []
    for el in lst1:
        if not el in lst2:
            list3.append(el)
    t_2 = perf_counter()
    return list3, t_2 - t_1


n = 10000
lst1 = [randint(0, int(n)) for i in range(n)]
lst2 = [randint(0, int(n)) for i in range(n)]

print(difference_set(lst1, lst2)[1])
print(difference_list(lst1, lst2)[1])
