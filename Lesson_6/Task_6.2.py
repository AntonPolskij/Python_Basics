# №6.2[41] Дан список, целых чисел.

# Напишите функцию, которая определит те элементы списка, у которых два соседних и, при этом, оба соседних элемента меньше данного.

# Функция

# Аргументы: список целых чисел

# Возвращает: список элементов(смотри условие)

# Примеры/Тесты:

# <function_name > ([1, 3, 3, 3, 5]) -> [5]

# <function_name > ([1, 5, 1, 6, 1]) -> [5, 6]

# <function_name > ([7, 5, 1, 6, 8]) -> [8]

# <function_name > ([8, 1, 5, 4, 5]) -> [8, 5]

def solution(lst: list) -> list:
    lst = []
    for i in range(len(lst1)):
        if i == len(lst1)-1:
            if lst1[i] > lst1[i-1] and lst1[i] > lst1[0]:
                lst.append(lst1[i])
        else:
            if lst1[i] > lst1[i-1] and lst1[i] > lst1[i+1]:
                lst.append(lst1[i])
    return lst


lst1 = [7, 5, 1, 6, 8]


print(solution(lst1))
