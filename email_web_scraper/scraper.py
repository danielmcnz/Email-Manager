#!/usr/bin/env python

from src.manager import *

import logging, os
from dotenv import load_dotenv

def main():
    create_logger()

    load_dotenv()
    directory = os.environ.get('DIR')
    print('started email transfer...')
    logging.info('started email transfer...')
    get_emails(directory, 'INBOX')

if __name__ == '__main__':
    main()