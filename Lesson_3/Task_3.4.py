# 3.4[23]. Дан список, состоящий из целых чисел. Напишите программу, которая сформирует список из тех элементов, которые больше предыдущего(элемента с предыдущим номером)

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# Примеры/Тесты:

# Input: [0, -1, 5, 2, 1]

# Output: [5]

# Input: [-2, -1, 5, 2, 3]

# Output: [-1, 5, 3]

# [*] Усложнение: Запишите алгоритм в одну строку, используйте Comprehension

list = [-2, -1, 5, 2, 3]

list_2 = []

list_3 = [list[i] for i in range(
    1, len(list)) if list[i] > list[i-1]]
print(list_3)

for i in range(1, len(list)):
    if list[i] > list[i-1]:
        list_2.append(list[i])

print(list_2)