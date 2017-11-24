from telephone_book_ctrl import action_add, action_del, action_get, action_upd, view_actions


def main():
    """
    telnet localhost 5001
    """

    while True:

        action = view_actions.input_message('Do you want to *get*, *add*, *upd* or *del* contact? '
                                            'Or *end* to finish: ')

        if action == 'get':
            action_get()
        elif action == 'add':
            action_add()
        elif action == 'upd':
            action_upd()
        elif action == 'del':
            action_del()
        elif action == 'end':
            return False
        else:
            print('There is no such action!')


if __name__ == '__main__':
    main()
