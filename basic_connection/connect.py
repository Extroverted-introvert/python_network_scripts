from multiprocessing.connection import wait
import socket
import logging
from time import sleep

class ServerClass:
    def server_connect(self, port):
        s = socket.socket()
        logging.info('Socket succesfully created')
        s.bind(('', port))
        logging.info(f'socket binded to port {port}')
        s.listen(5)
        logging.info('Socket is listening')
        while True:
            c, addr = s.accept()
            logging.info(f'Got connection from {addr}')
            message = ('Thank you for connecting')
            c.send(message.encode())
            c.close()
        return None    

class ClientClass:
    def client_connect(self, port):
        s = socket.socket()
        s.connect(('127.0.0.1', port))
        logging.info(s.recv(1024))
        sleep(100)
        s.close()