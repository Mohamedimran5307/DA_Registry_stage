from time import sleep

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configurations.config import Testdata
from Pageobjects.Loginpage import Loginpage
from Pageobjects.Support_Tickets import Support_Ticket_Page
from Testcases.confitest import init_driver
from Testcases.test_base import Basetest
from Pageobjects.AddParticipant_page import Participant_page


class Test_Settings_page(Basetest):

    @allure.description("Testing Support Ticket Page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Supoort_Ticket_Page(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        sleep(5)
        self.support_Ticket_page = Support_Ticket_Page(self.driver)
        self.support_Ticket_page.do_click(Support_Ticket_Page.SUPPORT_TICKET_ICON)
        sleep(5)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/support":
            allure.attach(self.driver.get_screenshot_as_png(), name="Support Ticket Icon is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Support Ticket Icon is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Support Ticket Icon is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Support Ticket Icon is invisible"
        self.datasets_page.do_click(Support_Ticket_Page.SIGN_OUT_BUTTON)
        print("Completed Test Case")