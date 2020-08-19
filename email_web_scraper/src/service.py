import os, enum

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

        self.exepath = os.getcwd+'/geckodriver'
        self.driver = ''

        if browser == Browsers.firefox:
            self.driver = webdriver.Firefox(executable_path=self.exepath)
        
        return self.driver

    def get_service_link(self):
        """ Opens chosen email website
        """

        if self.sel_serv == Services.now:
            self.driver.get('http://nowmail.co.nz')
        elif self.sel_serv == Services.gmail:
            self.driver.get('http://gmail.com')

    def login(self):
        """Logs into email account
        """

        load_dotenv()
        self.user = self.driver.find_element_by_id('rcmloginuser')
        self.user.send_keys(os.environ.get('USER'))
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

    def del_email(self):
        """Deletes currently selected email
        """

        if self.sel_serv == Services.now:
            self.delete = self.driver.find_element_by_id('rcmbtn123')
            self.delete.click()

        print('deleted {email}'.format(email=self.currentfile))
        logging.info('deleted {email}'.format(email=self.currentfile))

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