# 64.4[45] Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n(включая 1, но исключая само n) равна числу m и наоборот.

# Например, 220 и 284 – дружественные числа.

# 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, — их сумма равна 284.

# 284: 1, 2, 4, 71 и 142, — их сумма равна 220.

# Первые пары дружественных чисел:

# 220, 284
# 1184, 1210
# 2620, 2924
# 5020, 5564
# 6232, 6368

# Для заданного числа number выведите все пары дружественных чисел, каждое из которых не превосходит number.

# Напишите функцию:

# Аргументы: целое число

# Печатает все пары дружественных чисел, не превосходящих аргумент.

# Каждая пара должна быть выведена только один раз(перестановка чисел новую пару не дает).

# Примечание:

# 1. Выделите значимые куски алгоритма и оформите их в виде функций

# 2. Задокументируйте созданные функции

# 3. Используйте type hinting

# Примеры/Тесты:

# <function_name > (300)

# 220 284

# <function_name > (10000)

# 220 284

# 1184 1210

# 2620 2924

# 5020 5564

# 6232 6368

def sum_divisor(num: int) -> int:
    """return sum of divisior for number of num

    Args:
        a (int): number for ... calc sum

    Returns:
        int: sum of divisor
    """
    sum_a = 0
    for i in range(1, num):
        if num % i == 0:
            sum_a += i
    return sum_a


def find_friendly_numbers(number: int) -> None:
    """Print friendly_numbers in range of number

    Args:
        number (int): range for finding friendly_numbers
    """
    for i in range(1, number):
        sum_1 = sum_divisor(i)
        sum_2 = sum_divisor(sum_1)
        if i == sum_2 and i < sum_1:
            print(i, sum_1)


find_friendly_numbers(10000)
