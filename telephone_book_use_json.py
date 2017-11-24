import json


class ModelJSON:
    def __init__(self, contact_list):
        self.contact_list = contact_list

    def add_contact(self, name, number):
        self.contact_list[name] = number
        return self.contact_list

    def delete_contact(self, name):
        del self.contact_list[name]
        return self.contact_list

    def is_name_exists(self, name):
        return name in self.contact_list


class UseJSON:
    def __init__(self):
        self._json_file_name = 'book_in_json.json'

    def get_contacts(self):
        try:
            with open(self._json_file_name) as f:
                return json.load(f)
        except FileNotFoundError:
            print('"{}" file doesn\'t exist'.format(self._json_file_name))

    def write_phone_book(self, contacts_in_json):
        try:
            with open(self._json_file_name, 'w') as f:
                return json.dump(contacts_in_json, f, sort_keys=True, indent=4)
        except FileNotFoundError:
            print('"{}" file doesn\'t exist'.format(self._json_file_name))
