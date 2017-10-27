import json


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
