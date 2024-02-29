import time

from Pageobjects.Basepage import Basepage
from selenium.webdriver.common.by import By
from Configurations.config import Testdata


class Login_page(Basepage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.BASEURL)

    """ These are the page actions for the Add_participant_page"""

    def Username_login(self, USER_NAME, PASSWORD):
        self.do_click("USERNAME_FIELD_ID")
        self.do_type("USERNAME_FIELD_ID", USER_NAME)
        print("Hi")
        self.do_click_index("PASSWORD_XPATH", 0)
        print("Bye")
        self.do_type_index("PASSWORD_XPATH", 0, PASSWORD)
        # self.do_click("PASSWORD_XPATH")
        # self.do_type("PASSWORD_XPATH", PASSWORD)
        self.do_click("CHECKBOX_ID")
        self.do_click("SUBMIT_BUTTON_XPATH")
        time.sleep(2)

    """This is to get the Homepage title"""

    def get_Home_page_title(self, title):
        return self.get_title(title)
