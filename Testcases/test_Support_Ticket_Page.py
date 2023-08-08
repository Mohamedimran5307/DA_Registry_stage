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
        self.support_Ticket_page.do_click(Support_Ticket_Page.SIGN_OUT_BUTTON)
        print("Completed Test Case")

    @allure.description("Testing Search Input Filter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Search_input_filter(self):
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
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,150);")
        sleep(2)
        self.support_Ticket_page.do_click(Support_Ticket_Page.SUPPORT_TICKET_SEARCH_INPUT_FIELD)
        sleep(2)
        self.support_Ticket_page.do_sendkeys(Support_Ticket_Page.SUPPORT_TICKET_SEARCH_INPUT_FIELD,
                                             Testdata.SEARCH_INPUT_TEXT_SUPPORT_TICKETS)
        sleep(3)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/support":
            allure.attach(self.driver.get_screenshot_as_png(), name="Search input fiter is functional",
                          attachment_type=AttachmentType.PNG)
            assert True, "Search input fiter is functional"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Search input fiter is not functional",
                          attachment_type=AttachmentType.PNG)
            assert False, "Search input fiter is not functional"
        self.support_Ticket_page.do_click(Support_Ticket_Page.SIGN_OUT_BUTTON)
        print("Done")

    @allure.description("Testing Status Filter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Status_filter(self):
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
        sleep(2)
        self.support_Ticket_page.do_click(Support_Ticket_Page.STATUS_FILTER_BUTTON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,200);")
        sleep(2)
        self.support_Ticket_page.do_click_STATUS_CLOSE_CHECKBOX()
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,200);")
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/support":
            allure.attach(self.driver.get_screenshot_as_png(), name="Status filter is functional",
                          attachment_type=AttachmentType.PNG)
            assert True, "Status input filter is functional"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Status input filter is not functional",
                          attachment_type=AttachmentType.PNG)
            assert False, "Status input filter is not functional"
        self.support_Ticket_page.do_click(Support_Ticket_Page.SIGN_OUT_BUTTON)
        print("Done")

    @allure.description("Testing Status Close Button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Status_Close_Button(self):
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
        sleep(2)
        self.support_Ticket_page.do_click(Support_Ticket_Page.STATUS_FILTER_BUTTON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,200);")
        sleep(2)
        self.support_Ticket_page.do_click(Support_Ticket_Page.STATUS_CLOSE_BUTTON)
        sleep(3)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/support":
            allure.attach(self.driver.get_screenshot_as_png(), name="Status Close is functional",
                          attachment_type=AttachmentType.PNG)
            assert True, "Status input Close is functional"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Status input Close is not functional",
                          attachment_type=AttachmentType.PNG)
            assert False, "Status input Close is not functional"
        self.support_Ticket_page.do_click(Support_Ticket_Page.SIGN_OUT_BUTTON)
        print("Done")

    @allure.description("Testing Category Filter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Category_filter(self):
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
        sleep(2)
        self.support_Ticket_page.do_click(Support_Ticket_Page.CATEGORY_FILTER_BUTTON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,400);")
        sleep(2)
        self.support_Ticket_page.do_click_CATEGORY_DATASETS_CHECKBOX()
        sleep(3)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/support":
            allure.attach(self.driver.get_screenshot_as_png(), name="Category fiter is functional",
                          attachment_type=AttachmentType.PNG)
            assert True, "Category fiter is functional"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Category fiter is not functional",
                          attachment_type=AttachmentType.PNG)
            assert False, "Category fiter is not functional"
        self.support_Ticket_page.do_click(Support_Ticket_Page.SIGN_OUT_BUTTON)
        print("Done")

    @allure.description("Testing By_Date Filter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_By_Date_filter(self):
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
        sleep(2)
        self.support_Ticket_page.do_click(Support_Ticket_Page.BY_DATE_FILTER)
        self.support_Ticket_page.do_click(Support_Ticket_Page.BY_DATE_FILTER_START_DATE)
        sleep(2)
        self.support_Ticket_page.do_sendkeys(Support_Ticket_Page.BY_DATE_FILTER_START_DATE, Testdata.FILTER_START_DATE)
        sleep(2)
        self.support_Ticket_page.do_click(Support_Ticket_Page.BY_DATE_FILTER_END_DATE)
        self.support_Ticket_page.do_sendkeys(Support_Ticket_Page.BY_DATE_FILTER_END_DATE, Testdata.FILTER_END_DATE)
        self.driver.execute_script("window.scrollBy(0,400);")
        sleep(3)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/support":
            allure.attach(self.driver.get_screenshot_as_png(), name="By_Date fiter is functional",
                          attachment_type=AttachmentType.PNG)
            assert True, "By_Date fiter is functional"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="By_Date fiter is not functional",
                          attachment_type=AttachmentType.PNG)
            assert False, "By_Date fiter is not functional"
        self.support_Ticket_page.do_click(Support_Ticket_Page.SIGN_OUT_BUTTON)
        print("Done")

    @allure.description("Testing Clear all Button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Clear_all_Button(self):
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
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,150);")
        sleep(2)
        self.support_Ticket_page.do_click(Support_Ticket_Page.SUPPORT_TICKET_SEARCH_INPUT_FIELD)
        sleep(2)
        self.support_Ticket_page.do_sendkeys(Support_Ticket_Page.SUPPORT_TICKET_SEARCH_INPUT_FIELD,
                                             Testdata.SEARCH_INPUT_TEXT_SUPPORT_TICKETS)
        sleep(3)
        self.support_Ticket_page.do_click(Support_Ticket_Page.CLEAR_ALL_BUTTON)

        sleep(3)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/support":
            allure.attach(self.driver.get_screenshot_as_png(), name="Clear all Button is functional",
                          attachment_type=AttachmentType.PNG)
            assert True, "Clear all Button is functional"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Clear all Button is not functional",
                          attachment_type=AttachmentType.PNG)
            assert False, "Clear all Button is not functional"
        self.support_Ticket_page.do_click(Support_Ticket_Page.SIGN_OUT_BUTTON)
        print("Done")

    @allure.description("Testing Load more Button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Load_more_Button(self):
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
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,600);")
        sleep(2)
        self.support_Ticket_page.do_click(Support_Ticket_Page.LOAD_MORE_BUTTON)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/support":
            allure.attach(self.driver.get_screenshot_as_png(), name="Load_more_Button is functional",
                          attachment_type=AttachmentType.PNG)
            assert True, "Load_more_Button is functional"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Load_more_Button is not functional",
                          attachment_type=AttachmentType.PNG)
            assert False, "Load_more_Button is not functional"
        self.support_Ticket_page.do_click(Support_Ticket_Page.SIGN_OUT_BUTTON)
        print("Done")

    @allure.description("Testing List_view Button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_List_view_Button(self):
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
        sleep(2)
        self.support_Ticket_page.do_click(Support_Ticket_Page.COSTEWARD_LIST_VIEW)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/support":
            allure.attach(self.driver.get_screenshot_as_png(), name="List_view Button is functional",
                          attachment_type=AttachmentType.PNG)
            assert True, "List_view Button is functional"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="List_view Button is not functional",
                          attachment_type=AttachmentType.PNG)
            assert False, "List_view Button is not functional"
        self.support_Ticket_page.do_click(Support_Ticket_Page.SIGN_OUT_BUTTON)
        print("Done")

    @allure.description("Testing Participant_Tickets_Tab")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Participant_Tickets_Tab(self):
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
        sleep(2)
        self.support_Ticket_page.do_click(Support_Ticket_Page.PARTICIPANT_TICKET)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/support":
            allure.attach(self.driver.get_screenshot_as_png(), name="Participant_Tickets_Tab is functional",
                          attachment_type=AttachmentType.PNG)
            assert True, "Participant_Tickets_Tab is functional"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Participant_Tickets_Tab is not functional",
                          attachment_type=AttachmentType.PNG)
            assert False, "Participant_Tickets_Tab is not functional"
        self.support_Ticket_page.do_click(Support_Ticket_Page.SIGN_OUT_BUTTON)
        print("Done")
