import logging
import sys
from connect import ServerClass
logging.basicConfig(level = logging.INFO)

if __name__ == '__main__':
    input_args = sys.argv
    client = ServerClass()
    if len(input_args) <= 1:
        logging.info("No port found, initiating at 8000")
        port = 8000 # Set default pdf to process
    else:
        port = int(input_args[-1])
    logging.info('Input Port: %s' % port)
    client.server_connect(port)