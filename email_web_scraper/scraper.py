from manager import (fix_subject, 
                        get_emails, 
                        rename_emails,
                        create_logger)

import logging, os
from dotenv import load_dotenv

def main():
    create_logger()

    load_dotenv()
    directory = os.environ.get('DIR')
    print('started email transfer...')
    logging.info('started email transfer...')
    get_emails(directory, 'INBOX_Drafts')

if __name__ == '__main__':
    main()