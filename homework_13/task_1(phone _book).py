import sqlite3


def add_new_contact():
    with sqlite3.connect('phone_book.db') as connection:
        name = input('Введите имя: ')
        number = input('Введите номер: ')
        result = connection.execute('INSERT INTO phone_book VALUES(?, ?)', (name, number))
    print(f'Новый контакт {name} добавлен.')


def print_list_contacts():
    with sqlite3.connect('phone_book.db') as connection:
        result = connection.execute('SELECT * FROM phone_book ORDER BY name')
        for i in result.fetchall():
            print(i)


def update_contact():
    with sqlite3.connect('phone_book.db') as connection:
        name = input('Введите контакт, номер которого необходимо заменить: ')
        number = input('Введите новый номер: ')
        result = connection.execute('UPDATE phone_book SET number = ? WHERE name = ?', (number, name))
    print('Номер изменён.')


def main():
    print('Привет, это телефонная книга! \n'
          'Вот список поддерживаемых операций: \n'
          '  выйти из программы: 0 \n'
          '  добавить новый контакт: 1 \n'
          '  вывести весь список контактов в алфавитном порядке: 2 \n'
          '  обновить номер контакта: 3')

    while True:
        try:
            answer = int(input('Введите операцию: '))
            if answer == 0:
                print('Goodbye!!!')
                break
            if answer == 1:
                add_new_contact()
            if answer == 2:
                print_list_contacts()
            if answer == 3:
                update_contact()
        except ValueError:
            print('Введите 0 1 2 или 3')


if __name__ == '__main__':
    main()
