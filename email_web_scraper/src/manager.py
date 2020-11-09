from email.message import EmailMessage 
from email.parser import BytesParser
import os, logging
from datetime import date

from .emails import Driver

def fix_subject(filepath, filename):
    """Changes the name of the email file to the subject of the email

    Args:
        filepath (string): filepath of email
        filename (string): name of email file
    """

    file = open(filepath+filename, 'rb')
    msg = BytesParser().parse(file)
    subject = msg['subject']

    #day = msg['date'][5:7]
    #month = msg['date'][8:11]

    try:
        os.rename(filepath+filename, filepath+subject+".eml")
        print('renamed {file} to {newfile}'.format(file=filepath+filename, newfile=filepath+subject+".eml"))
        logging.info('renamed {file} to {newfile}'.format(file=filepath+filename, newfile=filepath+subject+".eml"))
    except:
        print('failed to rename {file}'.format(file=filepath+filename))
        logging.info('failed to rename {file}'.format(file=filepath+filename))

    file.close()

def get_emails(directory, email_folder):
    """Saves and removes emails

    Args:
        directory (string): directory for emails to be saved in
        email_folder (string): folder of emails in website
    """

    driver = Driver()
    driver.set_directory(directory)
    driver.login()
    driver.select_folder(email_folder)
    driver.sort_by_date('ascending')
    # driver.save_and_rm_emails()

def rename_emails(directory):
    """renames all email(s) in directory and subdirectories

    Args:
        directory (string): parent directory of email(s)
    """
    
    print('now renaming emails...')
    logging.info('now renaming emails...')

    files = os.listdir(directory)
    for file in files:
        fullPath = os.path.join(directory, file)
        if os.path.isdir(fullPath):
            rename_emails(fullPath+"/")
        else:
            fix_subject(directory,file)
            
    print('completed renaming emails...')
    logging.info('completed renaming emails...')

def create_logger():
    """Sets up the logger
    """
    
    count = 0
    if not os.path.exists('logging'):
        os.mkdir('logging')
    if not os.path.isfile('logging/email_transfer_{date}.log'.format(date=date.today())):
        logging.basicConfig(filename='logging/email_transfer_{date}.log'.format(date=date.today()), level=logging.INFO)
    else:
        while os.path.isfile('logging/email_transfer_{date}_{num}.log'.format(date=date.today(), num=count)):
            count += 1
        logging.basicConfig(filename='logging/email_transfer_{date}_{num}.log'.format(date=date.today(), num=count), level=logging.INFO)
