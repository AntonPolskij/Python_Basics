# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.  Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.

# Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9


list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
X = int(input('Введите число '))
nearest_num = 0

for i in list:
    if i > nearest_num:
        nearest_num = i

for i in list:
    if X < nearest_num:
        if i in range(X, nearest_num):
            nearest_num = i
    else:
        if i in range(nearest_num, X):
            nearest_num = i

print(nearest_num)
