# 3.2[19]. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность(сдвиг - циклический) на K элементов вправо, K – положительное число.

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# Примеры/Тесты:

# Input: [1, 2, 3, 4, 5] k = 3

# Output: [4, 5, 1, 2, 3]


n = [1, 2, 3, 4, 5]
list_2 = []
list_3 = []
k = 2

list_2 = n[k:] + n[:k]


for i in range(k, len(n)):
    list_3.append(n[i])

for i in range(k):
    list_3.append(n[i])

print(list_2)
print(list_3)
