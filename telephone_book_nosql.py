import datetime
from pymongo import MongoClient
from flask import g

client = MongoClient('localhost', 27017)
db = client.phone_book_db_new
collection = db['phone_book_db_new']


class ModelNoSQL:
    def __init__(self):
        self.posts = db.posts
        self.users = db.users
        self.sessions = db.sessions

    def add_contact(self, name, phone_number):
        post_data = {
            'name': name,
            'phone_number': phone_number,
            'date': datetime.datetime.utcnow(),
            'login': g.login
        }
        contact = self.posts.insert_one(post_data)
        return contact

    def get_contact(self, name):
        post_data = {
            'name': name,
            'login': g.login
        }
        contact = self.posts.find_one(post_data)
        try:
            return contact.get('phone_number')
        except AttributeError as e:
            print('Error {}. No contacts with name {} is found'.format(e, name))

    def update_in_table(self, name, phone_number):
        post_data = {
            '$set':
                {
                    'name': name,
                    'phone_number': phone_number,
                    'date': datetime.datetime.utcnow(),
                    'login': g.login
                }
            }
        result = self.posts.update_one({'name': name}, post_data)
        print(result.raw_result)
        return result.modified_count

    def delete_contact(self, name):
        post_data = {
            'name': name,
            'login': g.login
        }
        result = self.posts.delete_one(post_data)
        # print(result.deleted_count)
        return result.deleted_count

    def is_name_exists(self, name):
        post_data = {
            'name': name,
            'login': g.login
        }
        contact = self.posts.find_one(post_data)
        return bool(contact)

    def get_all_contacts(self):
        return self.posts.find({'login': g.login})

    def add_user(self, name, pwd):
        post_data = {
            'name': name,
            'password': pwd
        }
        self.users.insert_one(post_data)

    def get_user(self, name, pwd):
        post_data = {
            'name': name,
            'password': pwd
        }
        contact = self.users.find_one(post_data)
        print(contact)
        try:
            return contact
        except AttributeError as e:
            print('Error {}. No users with name {} is found'.format(e, name))

    def add_session(self, login, session_id):
        post_data = {
            'login': login,
            'session_id': session_id
        }
        self.sessions.insert_one(post_data)

    def get_session(self, session_id):
        post_data = {
            'session_id': session_id
        }
        return self.sessions.find_one(post_data)

    def lo(self):
        return self.posts.find({'login': g.login})
