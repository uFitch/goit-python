import pickle
import sys
import os.path

from classes import AddressBook, Record, Name, Phone


file = 'data.bin'


def input_error(func):
    def hundler(data):
        try:
            result = func(data)
        except Exception as e:
            return e
        return result
    return hundler


@input_error
def hello(data):
    print("How can I help you?")


@input_error
def add_func(data):
	data = data.replace('add ', '')
    if len(data.split()) == 2:
        name, phone = data.split()
        if name not in phone_book:
            phone_book[name] = phone
        else:
            raise Exception('This user already exists')
    else:
        raise Exception('Give me name and phone please')


@input_error
def change_func(data):
	data = data.replace('change ', '')
    if len(data.split()) == 2:
        name, phone = data.split()
        if name in phone_book:
            phone_book[name] = phone
        else:
            raise Exception('User is not found')
    else:
        raise Exception('Give me name and phone please')


@input_error
def phone_func(data):
    data = data.replace('phone ', '')
    if len(data.split()) == 1:
        name = data
        if name in phone_book:
            return phone_book[name]
        else:
            raise Exception('User is not found')
    else:
        raise Exception('Give me only name')


@input_error
def show_all_func(data):
    str_phone_book = [' '.join(el) for el in phone_book.items()]
    return '\n'.join(str_phone_book)


@input_error
def find(data):
    data = data.replace('find ', '')
    if len(data.split()) == 1:
        result = phone_book.full_search(data)
        return result


@input_error
def exit_func(data):
    with open(file, 'wb') as f:
        pickle.dump(phone_book, f)
    return "Good bye!"


OPERATIONS = {
    'hello': hello_func,
    'add': hello_func,
    'change': change_func,
    'phone': phone_func,
    'show all': show_all_func,
    'good bye': exit_func,
    'close': exit_func,
    'exit': exit_func
}


@input_error
def choice_action(data):
    for command in OPERATIONS:
        if data.startswith(command):
            return OPERATIONS[command]
    raise Exception('Give me a correct command')


def main():
    phone_book = AddressBook()
    if os.path.isfile(file):
        with open(file, 'rb') as f:
            phone_book = pickle.load(f)
    while True:
        data = input()

        func = choice_action(data)
        if isinstance(func, Exception):
            print(func)
            continue
        result = func(data)
        if result:
            print(result)
        if result == 'Good bye!':
            break

if __name__ == '__main__':
    main()