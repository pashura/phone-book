
class Model:
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

