from time import sleep

import pytest
import allure

from Configurations.config import Testdata
from Pageobjects.Login_page import Login_page
from Testcases.confitest import init_driver
from Testcases.test_base import Basetest

from allure_commons.types import AttachmentType


class Test_login(Basetest):

    @allure.description("Testing Homepage Title")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Home_page_title(self):
        self.Homepage = Login_page(self.driver)
        self.driver.maximize_window()
        title = self.Homepage.get_Home_page_title(Testdata.HOMEPAGE_TITLE)
        print(title)

        if self.driver.title == "DA Registry":
            allure.attach(self.driver.get_screenshot_as_png(), name="Valid Homepage",
                          attachment_type=AttachmentType.PNG)
            assert True, "Valid Homepagee"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Invalid Homepage",
                          attachment_type=AttachmentType.PNG)
            assert False, "Invalid Homepage"
        print("Completed")

    @allure.description("Testing Log in functionality")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_as_admin(self):
        login_page = Login_page(self.driver)
        sleep(3)
        self.driver.maximize_window()
        # self.driver.execute_script("window.localStorage.clear();")
        # sleep(3)
        # self.driver.execute_script("window.location.reload(true);")

        login_page.Username_login(Testdata.USER_NAME,Testdata.PASSWORD)
        if self.driver.current_url == "https://stage.digiext.org/da/dashboard":
            allure.attach(self.driver.get_screenshot_as_png(), name="Login is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Login is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, "Login is failed"
        print("Completed")

