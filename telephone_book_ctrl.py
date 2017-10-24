import configparser

from telephone_book_model import Model
from telephone_book_view import Communication
from telephone_book_use_json import UseJSON
from telephone_book_use_csv import UseCSV


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
else:
    raise Exception('Format {} doesn\'t exist'.format(used_format))

get_contact_list = use_storage.get_contacts()
my_actions = Model(get_contact_list)
view_actions = Communication()


def action_get(contact_list):
    name = view_actions.input_message('Please write <contact name>: ')
    if my_actions.is_name_exists(name):
        view_actions.print_message(contact_list[name])
    else:
        view_actions.print_message('{} is not found in phone book', name)


def action_add(contact_list):
    name_phone = view_actions.input_message('Please write <contact name>:<phone number>: ')
    name, phone = name_phone.split(':')
    if not my_actions.is_name_exists(name):
        my_actions.add_contact(name, phone)
        use_storage.write_phone_book(contact_list)
    else:
        view_actions.print_message('{} is already in phone book', name)


def action_upd(contact_list):
    name_phone = view_actions.input_message('Please write <contact name>:<phone number>: ')
    name, phone = name_phone.split(':')
    if not my_actions.is_name_exists(name):
        resp = view_actions.input_message('{} is not found in phone book. Do you want to add it? (Yes/No)', name)
        if resp == 'Yes':
            my_actions.add_contact(name, phone)
            use_storage.write_phone_book(contact_list)
        elif resp == 'No':
            pass
        else:
            while resp not in ['Yes', 'No']:
                resp = view_actions.input_message('Yes/No only supports: ')
            else:
                my_actions.add_contact(name, phone)
                use_storage.write_phone_book(contact_list)
    else:
        my_actions.add_contact(name, phone)
        use_storage.write_phone_book(contact_list)


def action_del(contact_list):
    name = view_actions.input_message('Please write <contact name>: ')
    if my_actions.is_name_exists(name):
        my_actions.delete_contact(name)
        use_storage.write_phone_book(contact_list)
    else:
        view_actions.print_message('{} is not found in phone book', name)



