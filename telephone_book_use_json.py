import json


class UseJSON:
    def __init__(self):
        self._json_file = json.dumps({})
        try:
            with open('book_in_json1.json') as f:
                self._json_file = f.read()
        except FileNotFoundError:
            print('ssssss')

    def get_contacts(self):
        return json.load(self._json_file)

    def write_phone_book(self, contacts_in_json):
        return json.dump(contacts_in_json, self._json_file, sort_keys=True, indent=4)


