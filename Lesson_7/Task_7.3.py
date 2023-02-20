# 7.3[  # ]. Имея список вида [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]

#     преобразовать его в списки вида

#     1)['Иванов-И-И', 'Петров-П-П', 'Соколов-И-Г'...]

# 2)['Иванов И.И.', 'Петров П.П.', 'Соколов И.Г.'...]

#     с использованием Comprehension; Comprehension + функция; Comprehension + lambda ; map

#     [**] Усложнение. Дополнить обработку списка условием: Выбираем только те элементы, в которых первая буква П


lst = [['Иванов', 'Иван', 'Иванович'], [
    'Петров', 'Петр', 'Петрович'], ['Соколов', 'Илья', 'Петрович']]


def template1(man):
    surname, name, parent = man
    return f'{surname} {name[0]}. {parent[0]}.'


def filter1(man):
    surname, name, parent = man
    if surname[0] == 'П':
        return True
    return False
# # lst4 = [template1(surname, name, parent) for surname, name, parent in lst]


lst4 = [(lambda surname, name, parent: f'{surname} {name[0]}. {parent[0]}.')(
    surname, name, parent) for surname, name, parent in lst if surname[0] == 'П']


lst5 = list(map(template1, filter(filter1, lst)))


print(lst4, lst5)
