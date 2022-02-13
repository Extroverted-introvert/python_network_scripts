import logging
import sys
from socket_basic import SocketConnection


if __name__ == '__main__':
    input_args = sys.argv
    socket = SocketConnection()
    if len(input_args) <= 1:
        logging.info("No address found, getting Host for www.google.com")
        address = "www.google.com" # Set default pdf to process
    else:
        address = str(input_args[-1])
    logging.info('Input Address: %s' % address)
    host = socket.fetch_host_name(address, port=80)
    print(host)
