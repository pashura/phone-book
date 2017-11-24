import configparser

from telephone_book_mysql import ModelMySQL
from telephone_book_view import Communication
from telephone_book_use_json import UseJSON, ModelJSON
from telephone_book_use_csv import UseCSV
from telephone_book_nosql import ModelNoSQL


config = configparser.ConfigParser()

try:
    config.read('config.ini')
    used_format = config['File']['Format']
except KeyError:
    raise Exception('Config file is incorrect')

if used_format == 'csv':
    use_storage = UseCSV()
elif used_format == 'json':
    use_storage = UseJSON()
    # my_actions = ModelJSON()
elif used_format == 'mysql':
    # use_storage = UseJSON()
    my_actions = ModelMySQL()
elif used_format == 'nosql':
    my_actions = ModelNoSQL()
else:
    raise Exception('Format {} doesn\'t exist'.format(used_format))

view_actions = Communication()


def action_get():
    name = view_actions.input_message('Please write <contact name>: ')
    if my_actions.is_name_exists(name):
        view_actions.print_message(my_actions.get_contact(name))
    else:
        view_actions.print_message('{} is not found in phone book', name)


def action_add():
    name_phone = view_actions.input_message('Please write <contact name>:<phone number>: ')

    try:
        name, phone = name_phone.split(':')
    except ValueError as e:
        print(e)
        return

    if not my_actions.is_name_exists(name):
        my_actions.add_contact(name, phone)
        # use_storage.write_phone_book(contact_list)
    else:
        view_actions.print_message('{} is already in phone book', name)


def action_upd():
    name_phone = view_actions.input_message('Please write <contact name>:<phone number>: ')

    try:
        name, phone = name_phone.split(':')
    except ValueError as e:
        print(e)
        return

    if not my_actions.is_name_exists(name):
        resp = view_actions.input_message('{} is not found in phone book. Do you want to add it? (Yes/No)', name)
        if resp == 'Yes':
            my_actions.add_contact(name, phone)
            # use_storage.write_phone_book(contact_list)
        elif resp == 'No':
            my_actions.update_in_table(name, phone)
        else:
            while resp not in ['Yes', 'No']:
                resp = view_actions.input_message('Yes/No only supports: ')
            else:
                if resp == 'Yes':
                    my_actions.add_contact(name, phone)
                else:
                    my_actions.update_in_table(name, phone)
                    print('Contact {} has been updated'.format(name))
    else:
        my_actions.update_in_table(name, phone)
        # use_storage.write_phone_book(contact_list)


def action_del():
    name = view_actions.input_message('Please write <contact name>: ')
    if my_actions.is_name_exists(name):
        my_actions.delete_contact(name)
        # use_storage.write_phone_book(contact_list)
    else:
        view_actions.print_message('{} is not found in phone book', name)



