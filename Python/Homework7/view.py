

commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']


def main_menu():
    print('Главное меню')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    choice = int(input('Выберите пункт меню: '))
    return choice

def show_contacts(phone_list: list):
    if len(phone_list) < 1: 
        print('телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')
        print()

def input_error():
    print('Ошибка ввода, введите корректный пункт меню')


def create_new_contact():
    name = input('Введите Имя и Фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def find_contact():
    find = input('Введите поисковой запрос: ')
    return find

def trash_contact():
    trash = input('Введите Имя или фамилию, которые хотите удалить: ')
    return trash

def change_contact():
    check = input('Введите Имя или фамилию контакта для изменения: ')
    change = input('Заполните контакт полностью с учетом изменений')
    return check, change
