# 2.1[9]. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N(произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# Примеры/Тесты:

# 5 -> Факториал 5 равен 120

# 0 -> Факториал 0 равен 1


n = int(input('Введите число '))
fact = 1

# while i <= n:
#     fact *= i
#     i += 1


for i in range(1, n + 1):
    fact *= i

print(fact)
