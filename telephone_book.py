from telephone_book_ctrl import action_add, action_del, action_get, action_upd, get_contact_list, view_actions


def main():
    contact_list = get_contact_list

    while True:
        action = view_actions.input_message('Do you want to *get*, *add* ot *del* contact? Or *end* to finish: ')

        if action == 'get':
            action_get(contact_list)
        elif action == 'add':
            action_add(contact_list)
        elif action == 'upd':
            action_upd(contact_list)
        elif action == 'del':
            action_del(contact_list)
        elif action == 'end':
            return False
        else:
            print('There is no such action!')

        view_actions.print_message('Available contact names: {}', ', '.join(i for i in contact_list))  # phone


if __name__ == '__main__':
    main()
