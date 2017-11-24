import sqlite3

DB_NAME = 'db.sqlite3'
TABLE_NAME = 'phone_book'


class ModelMySQL:
    db = sqlite3.connect(DB_NAME)

    def __init__(self):
        self.cursor = ModelMySQL.db.cursor()
        # self.contact_list = contact_list

    #  ready
    def add_contact(self, name, phone_number):
        self.cursor.execute("INSERT INTO phone_book (name, number) VALUES (?, ?)", (name, phone_number))
        ModelMySQL.db.commit()

    #  ready
    def get_contact(self, name):
        names = self.cursor.execute("SELECT number FROM phone_book WHERE (name = ?)", (name,))
        return names.fetchone()[0]

    def update_in_table(self):
        pass
        # self.cursor.execute("UPDATE INTO phone_book WHERE (name=?, number=?)", (name, phone_number))
        # Model.db.commit()

    #  ready
    def delete_contact(self, name):
        self.cursor.execute("DELETE FROM phone_book WHERE (name = ?)", (name,))
        ModelMySQL.db.commit()

    def is_name_exists(self, name):
        names = self.cursor.execute("SELECT name FROM phone_book WHERE (name = ?)", (name,))
        return name in [a[0] for a in names.fetchall()]
