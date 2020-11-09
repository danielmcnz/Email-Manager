from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os, enum, time, logging, platform

from dotenv import load_dotenv

class Services(enum.Enum):
    """ Enum of all supported services
    """
    now = 0
    gmail = 1

class Browsers(enum.Enum):
    """ Enum of all supported browsers
    """
    firefox = 0

class Service():
    def __init__(self, sel_service, browser):
        self.sel_serv = sel_service
        self.browser = browser

    def driver_setup(self):
        """Selects the browser for selenium to use and sets up selenium driver

        Returns:
            [string]: [handle to the selenium driver]
        """

        if platform.system() == 'Linux':
            self.exepath = os.getcwd()+os.sep()+'email_web_scraper'+os.sep()+'geckodriver'
        elif platform.system() == 'Windows':
            self.exepath = os.getcwd()+os.sep()+'email_web_scraper'+os.sep()+'geckodriver.exe'
        self.driver = ''

        if self.browser == Browsers.firefox:
            self.driver = webdriver.Firefox(executable_path=self.exepath)

        return self.driver

    def get_service_link(self):
        """ Opens chosen email website
        """

        if self.sel_serv == Services.now:
            self.driver.get('http://nowmail.co.nz')
        elif self.sel_serv == Services.gmail:
            self.driver.get('http://gmail.com')

    def sort_by_date(self, sort_type):
        """ Determines how the emails are sorted (ascending or descending)
        """

        self.date = self.driver.find_element_by_id('rcmdate')
        self.date.click()
        # if sort_type == 'ascending' :
        #     print('ascending')
        #     if not self.driver.find_elements_by_class_name('date sortedASC'):
        #         self.date.click()
        # elif sort_type == 'descending':
        #     print('descending')
        #     if not self.driver.find_elements_by_class_name('date sortedDESC'):
        #         self.date.click()

    def login(self):
        """Logs into email account
        """

        load_dotenv()
        self.user = self.driver.find_element_by_id('rcmloginuser')
        self.user.send_keys(os.environ.get('EMAIL'))
        self.pwd = self.driver.find_element_by_id('rcmloginpwd')
        self.pwd.send_keys(os.environ.get('PASSWORD'))
        self.submit = self.driver.find_element_by_css_selector(".button.mainaction[value='Login']")
        self.submit.click()

    def select_folder(self, folder_name):
        """Selects email folder

        Args:
            folder_name (string): name of email folder
        """

        time.sleep(6)
        if self.sel_serv == Services.now:
            if folder_name != 'INBOX':
                self.submit = self.driver.find_element_by_id("rcmli{folder}".format(folder=folder_name))
                self.submit.click()

    def select_first_email(self):
        """Selects first email in folder
        """

        time.sleep(1)

        if self.sel_serv == Services.now:
            self.email = self.driver.find_elements_by_class_name('date')
            self.email[1].click()

    def get_next_page(self):
        """Gets the next page of emails
        """

        if self.sel_serv == Services.now:
            self.next = self.driver.find_element_by_id('rcmbtn115')
            self.next.click()
            self.page_try = 1

        return self.page_try

    def del_email(self, currentfile):
        """Deletes currently selected email
        """

        if self.sel_serv == Services.now:
            self.delete = self.driver.find_element_by_id('rcmbtn123')
            self.delete.click()

        print('deleted {email}'.format(email=currentfile))
        logging.info('deleted {email}'.format(email=currentfile))

    def get_source(self):
        """ Opens the source of the email
        """

        if self.sel_serv == Services.now:
            self.settings = self.driver.find_element_by_id('messagemenulink')
            self.settings.click()
            time.sleep(1)
            self.source = self.driver.find_element_by_id('rcmbtn131')
            self.source.click()
            time.sleep(1)