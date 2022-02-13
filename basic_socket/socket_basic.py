'''Socket Programming in Python'''
import socket
import sys
import logging

class SocketConnection:
    def connect_socket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            logging.info('Socket succesfully created!')
            return s
        except socket.error as err:
            logging.error(f'Socket creation failed with error {err}')
    
    def fetch_host_name(self, address, port):
        try:
            host_ip = socket.gethostbyname(address)
        except socket.gaierror:
            logging.error('Error resolving the host')
            sys.exit()
        self.connect_socket().connect((host_ip, port))
        print(f'Socket has succesfully connected to {address} on port == {host_ip}')
        return host_ip