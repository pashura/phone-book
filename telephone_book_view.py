import socket


s = socket.socket()
s.bind(('127.0.0.1', 5002))
print("Server starts.. Port: {}".format(s.getsockname()[1]))
s.listen(5)
c, a = s.accept()


class Communication:
    def __init__(self):
        pass

    @staticmethod
    def input_message(message, *args):
        c.sendall(str(message.format(*args)).encode('utf-8'))
        in_message = c.recv(1024).decode()
        return in_message.strip()

    @staticmethod
    def print_message(message, *args):
        c.sendall(str(message.format(*args)).encode('utf-8'))
        c.sendall(b'\n')

