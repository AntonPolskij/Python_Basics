# 3.1[17]. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# Примеры/Тесты:

# [1, 1, 2, 0, -1, 3, 4, 4] -> 6

# [1, 1, 2, 0, 1, 2, 1, 2] -> 3


list = [1, 1, 2, 0, 1, 2, 1, 2]

sum_of_diff_nums = len(set(list))

print(sum_of_diff_nums)
