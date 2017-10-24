import json


class UseJSON:
    def __init__(self):
        self._json_file = 'book_in_json.json'
        # try:
        #     with open('book_in_json1.json') as f:
        #         self._json_file = f.read()
        # except FileNotFoundError:
        #     print('ssssss')

    def get_contacts(self):
        with open(self._json_file) as f:
            return json.load(f)

    def write_phone_book(self, contacts_in_json):
        with open(self._json_file) as f:
            return json.dump(contacts_in_json, f, sort_keys=True, indent=4)


