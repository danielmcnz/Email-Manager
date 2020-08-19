from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time, os, logging

from service import Service, Services


class Driver():
    def __init__(self, del_emails=False, service=Services.now):
        self.del_emails = del_emails
        self.service = Service(service)
        
        self.msgnum = 0
        self.page_try = 0
        self.emails_per_page = 100
        self.currentfile = ''
        self.subject = ''
        self.curdir = ''
        self.originaldir = ''

        self.driver = self.service.initialize()
        self.service.get_service_link()

    def set_emails_per_page(self, amount):
        """Sets the amount of emails allowed per folder in saved directory

        Args:
            amount (int): amount of emails per folder when email is saved
        """

        self.emails_per_page = amount

    def set_directory(self, directory):
        """Sets selected directory for emails to be saved in

        Args:
            directory (string): directory for emails to be saved in
        """

        self.originaldir = directory

    def login(self):
        """ Calls service login
        """

        self.service.login()

    def select_folder(self, folder_name):
        """Selects email folder

        Args:
            folder_name (string): name of email folder
        """

        self.service.select_folder(folder_name)

    def select_first_email(self):
        """Selects first email in folder
        """

        self.service.select_first_email()

    def get_next_page(self):
        """Gets the next page of emails
        """

        self.page_try = self.service.get_next_page()

    def del_email(self):
        """Deletes currently selected email
        """

        if(self.del_emails):
            self.service.del_email()

    def get_source(self):
        """ Opens the source of the email
        """

        self.service.get_source()

    def save_email(self, text):
        """Saves currently selected email in specified filepath

        Args:
            text (string): contents of email
        """

        if self.msgnum % self.emails_per_page == 0:
            if not os.path.exists(self.originaldir+'messages{num}/'.format(num=str(int(self.msgnum/self.emails_per_page)))):
                self.curdir = self.originaldir+'messages{num}/'.format(num=str(int(self.msgnum/self.emails_per_page)))
                os.mkdir(self.curdir)
            else:
                while os.path.exists(self.originaldir+'messages{num}/'.format(num=str(int(self.msgnum/self.emails_per_page)))):
                    self.msgnum += 1
                self.curdir = self.originaldir+'messages{num}/'.format(num=str(int(self.msgnum/self.emails_per_page)))
                os.mkdir(self.curdir)
        
        self.currentfile = self.curdir+'msg{num}.eml'.format(num=self.msgnum)
        self.file = open(self.currentfile, 'x')
        self.file.write(self.text)
        self.file.close()
        print('saved {file}'.format(file=self.currentfile))
        logging.info('saved {file}'.format(file=self.currentfile))
        self.msgnum += 1

    def save_and_rm_emails(self):
        """Main loop for selecting, saving and deleting emails
        """
        self.loop = True

        try:
            self.select_first_email()
            self.loop = True
        except:
                if self.page_try == 0:
                    print('next page')
                    logging.info('next page')
                    self.get_next_page()
                    time.sleep(5)
                    self.loop = True
                else:
                    print('file transfer completed')
                    logging.info('file transfer completed')
                    self.loop = False

        while self.loop:
            self.get_source()

            try:
                self.driver.switch_to.window(self.driver.window_handles[1])
                self.page_try = 0
            except:
                if self.page_try == 0:
                    print('next page')
                    logging.info('next page')
                    self.get_next_page()
                    time.sleep(5)
                    continue
                else:
                    print('file transfer completed')
                    logging.info('file transfer completed')
                    break
                
            self.page_source = self.driver.find_element_by_tag_name('body')
            self.text = self.page_source.get_attribute('innerText')
            
            self.save_email(self.text)

            self.driver.close()

            self.driver.switch_to.window(self.driver.window_handles[0])
            self.del_email()