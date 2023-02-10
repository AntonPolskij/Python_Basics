# 4.1[22]: Даны два неупорядоченных набора целых чисел(может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Если таких чисел нет - выдать внятное диагностическое сообщение

# 	Примеры/Тесты:
#     Input1: 2 4 6 8 10 12 10 8 6 4 2
#     Input2: 3 6 9 12 15 18
#     Output: 6 12     Обратите внимание: Без скобочек, в одну строку

#     Input1: 2 4 6 8 10 10 8 6 4 2
#     Input2: 3 9 12 15 18
#     Output: Повторяющихся чисел нет

list1 = str('2 4 6 8 10 10 8 6 4 2').split(' ')
list2 = str('3 9 12 15 18').split(' ')

solution_set = set()

solution_out = ''

for i in list1:
    if i in list2:
        solution_set.add(i)

if len(solution_set) == 0:
    print('Повторяющихся чисел нет')
else:
    for el in solution_set:
        solution_out += f'{int(el)} '
    print(solution_out)