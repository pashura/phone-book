
class Communication:
    def __init__(self):
        pass

    @staticmethod
    def input_message(message, *args):
        return input(message.format(*args))

    @staticmethod
    def print_message(message, *args):
        print(message.format(*args))

