import hashlib
import random
import string
from flask import Flask, render_template, request, redirect, session, g
from telephone_book_nosql import ModelNoSQL


app = Flask(__name__)
app.secret_key = 'g#UIUBV$GYtR5^UT56uI&^%tsfdshbd327dh'


@app.before_request
def before_request():
    g.login = None
    g.my_actions = ModelNoSQL()
    if 'session_id' in request.cookies:
        print('Session ID = ' + request.cookies['session_id'])
        try:
            user = g.my_actions.get_session(request.cookies['session_id'])['login']
            g.login = user
        except:
            pass


def encrypt_password(password):
    h = hashlib.sha256()
    h.update(password.encode('utf8'))
    return h.hexdigest()


def create_session_id():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(128))


def get_all_contacts():
    all_contacts = g.my_actions.get_all_contacts()
    return [{'name': contact['name'],
            'phone_number': contact['phone_number']}
            for contact in all_contacts]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_ = request.form.get('login', '')
        pwd = encrypt_password(request.form.get('pwd', ''))
        user = g.my_actions.get_user(login_, pwd)
        session_id = ''
        if user:
            session_id = create_session_id()
            g.my_actions.add_session(login_, session_id)
        # print('login/pwd/user = ' + login_, pwd, user)
        response = app.make_response(redirect('/action'))
        # print('respons = ' + str(response))
        response.set_cookie('session_id', session_id, httponly=True)
        return response
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        login_ = request.form.get('login', '')
        pwd1 = request.form.get('pwd1', '')
        pwd2 = request.form.get('pwd2', '')
        if login_ and pwd1 and pwd1 == pwd2:
            g.my_actions.add_user(login_, encrypt_password(pwd1))
            return redirect('/')
    return render_template('signup.html')


@app.route('/action')
def action():
    all_contacts = get_all_contacts()

    message = session.pop('result', '')
    return render_template('action.html', message=message, all_contacts=all_contacts)


@app.route('/get/', methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        name = request.form.get('desc', '')
        phone = g.my_actions.get_contact(name)
        session['result'] = 'Phone number of {} is {}'.format(name, phone)
        return redirect('/action')
    return render_template('get.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # name_phone = request.form.get('desc', '').split(':')
        name = request.form.get('name', '')
        phone_number = request.form.get('number', '')
        g.my_actions.add_contact(name, phone_number)
        contact = ':'.join(name)
        session['result'] = 'Contact {} has been successfully added'.format(contact)
        return redirect('/action')
    return render_template('add.html')


@app.route('/upd', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        name_phone = request.form.get('desc', '').split(':')
        g.my_actions.update_in_table(name_phone[0], name_phone[1])
        contact = ':'.join(name_phone)
        session['result'] = 'Contact {} has been successfully updated'.format(contact)
        return redirect('/action')
    return render_template('upd.html')


@app.route('/del', methods=['GET', 'POST'])
def delete():
    all_contacts = get_all_contacts()
    if request.method == 'POST':
        name = request.form.get('desc', '')
        g.my_actions.delete_contact(name)
        session['result'] = 'Contact {} has been successfully removed'.format(name)
        return redirect('/action')
    return render_template('del.html', all_contacts=all_contacts)


if __name__ == '__main__':
    app.run(debug=True)
