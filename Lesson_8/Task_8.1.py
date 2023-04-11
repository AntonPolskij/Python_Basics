# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2)CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller
from pathlib import Path
MAIN_DIR = Path(__file__).parent

# phone_book = {123: ('Польский', 'Антон', '99912345', 'друг'),
#               124: ('Петров', 'Иван', '88843210', 'враг')}

phone_book = []


def menu(data: list):
    while True:
        print('Выберите действие')
        print('1 - Создать новую запись')
        print('2 - Распечатать содержимое справочника')
        print('3 - Найти человека в справочнике')
        print('4 - Импортировать данные с текстового файла')
        print('5 - Загрузить справочник в текстовый файл')
        get = input('Введите действие: ')
        if get == '':
            print()
            print('До свидания')
            return False
        elif get == '1':
            # Добавляет запись в существующую телефонную книгу.
            data = create(data, get_data())
        elif get == '2':
            print_phone_book(data)
        elif get == '3':
            find_name = str(
                input('Введите фамилию или первые буквы фамилии: '))
            find_value = find_human(data, find_name)
            print(find_value)
            print('Удалить запись: 1')
            print('Изменить данные: 2')
            print('Возврат: Enter')
            input_value = input()
            if input_value == '1':
                delete_value(data, find_value)
            elif input_value == '2':
                print('Изменить фамилию - 1')
                print('Изменить имя - 2')
                print('Изменить телефон - 3')
                print('Изменить описание - 4')
                print('Возврат в главное меню: Enter')
                input_value = int(input())
                change_value(input_value, find_value, data)
        elif get == '4':
            name_file = get_file_name()
            batch_data = get_batch_data(name_file)
            data = batch_create(data, batch_data)
        elif get == '5':
            name_file = input('Введите название файла')
            write_file(data, name_file)


def create(data: list, elem: tuple) -> list:
    data.append(elem)
    return data


def print_phone_book(data: list) -> None:
    for value in data:
        print(value)


def get_data() -> tuple:  # запрашивает данные у пользователя
    surname = input('Введите фамилию: ')
    name = input('Введите Имя: ')
    phone = input('Введите телефон: ')
    description = input('Введите описание: ')
    return (surname, name, phone, description)


def get_file_name() -> str:
    return input('Введите имя файла: ')


def get_batch_data(name_file: str) -> list:
    lst = []
    with open(MAIN_DIR / name_file, 'r', encoding='utf-8') as file:
        for line in file:
            temp = tuple(line.strip().split('#'))
            lst.append(temp)
    return lst


def write_file(phone_book: list, file_name: str):
    with open(MAIN_DIR / f'{file_name}.txt', 'w', encoding='utf-8') as file:
        for element in phone_book:
            template = f'{element[0]}#{element[1]}#{element[2]}#{element[3]}\n'
            file.write(template)


def batch_create(data, batch_data) -> list:
    for human in batch_data:
        data = create(data, human)
    return data


def find_human(phone_book: list, surname: str):
    surname = surname.lower()
    for el in phone_book:
        if el[0].lower().startswith(surname):
            return el


def delete_value(phone_book, value):
    phone_book.remove(value)


def change_value(operation: int, value: tuple, data: list):
    index_in_data = data.index(value)
    lst_value = [*value]
    lst_value[operation-1] = input('Введите новое значение')
    data[index_in_data] = tuple(lst_value)
    return data


menu(phone_book)
