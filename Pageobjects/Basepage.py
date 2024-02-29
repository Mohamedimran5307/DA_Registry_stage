import logging

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
from Configurations.config import Testdata
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from Utilities import configReader
from Utilities.Logutilities import Logger

log = Logger(__name__, logging.INFO)
"""This is parent class of the pages (Login page)"""

"""It contains all the generic methods and Utilities for all the pages"""

"""Set of supported locator strategies."""


# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"


class Basepage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("NAME"):
            self.driver.find_element(By.NAME, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("CSS_SELECTOR"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            # print("REACHED", locator)
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).click()
        log.logger.info("Clicking on element: " + str(locator))

    # def do_click(self, locator, text_value=None):
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("NAME"):
    #         self.driver.find_element(By.NAME, configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("CLASS_NAME"):
    #         self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("CSS_SELECTOR"):
    #         self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("_TEXT") and text_value is not None:
    #         # Construct XPath expression to find element by text and click it
    #         xpath_expression = f"//*[contains(text(), '{text_value}')]"
    #         self.driver.find_element(By.XPATH, xpath_expression).click()
    #     else:
    #         log.logger.info(f"Locator type '{locator}' is not supported or text value is missing.")
    #     log.logger.info("Clicking on element: " + str(locator))

    def do_click_ORDER(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(by_locator))

    def do_click_index(self, locator, index):
        wait = WebDriverWait(self.driver, 10)
        if str(locator).endswith("_XPATH"):
            elements = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, configReader.readConfig("locators", locator))))
            elements[index].click()
        elif str(locator).endswith("NAME"):
            self.driver.find_elements(By.NAME, configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("CLASS_NAME"):
            self.driver.find_elements(By.CLASS_NAME, configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("CSS_SELECTOR"):
            self.driver.find_elements(By.CSS_SELECTOR, configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ID"):
            self.driver.find_elements(By.ID, configReader.readConfig("locators", locator))[index].click()
        log.logger.info("Clicking on element" + str(locator) + "with index:" + str(index))

    def do_type_index(self, locator, index, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements(By.XPATH, configReader.readConfig("locators", locator))[index].send_keys(value)
        elif str(locator).endswith("NAME"):
            self.driver.find_elements(By.NAME, configReader.readConfig("locators", locator))[index].send_keys(value)
        elif str(locator).endswith("CLASS_NAME"):
            self.driver.find_elements(By.CLASS_NAME, configReader.readConfig("locators", locator))[index].send_keys(
                value)
        elif str(locator).endswith("CSS_SELECTOR"):
            self.driver.find_elements(By.CSS_SELECTOR, configReader.readConfig("locators", locator))[index].send_keys(
                value)
        elif str(locator).endswith("_ID"):
            self.driver.find_elements(By.ID, configReader.readConfig("locators", locator))[index].click()
        log.logger.info("Clicking on element" + str(locator) + "with index:" + str(index))

    def do_type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("NAME"):
            self.driver.find_element(By.NAME, configReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("CSS_SELECTOR"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing in an element" + "Entering the value as:" + value)

    def get_Text(self, locator):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("NAME"):
            text = self.driver.find_element(By.NAME, configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("CLASS_NAME"):
            text = self.driver.find_element(By.CLASS_NAME, configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("CSS_SELECTOR"):
            text = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ID"):
            text = self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).text
        log.logger.info("Getting text from an element" + str(locator))
        return text

    def do_swipeUp(self, howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 600, 514, 200, 1000)


    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    #  def do_sendkeys_1(self):
    #     # Get the absolute path to the current working directory
    #     current_directory = os.getcwd()
    #
    #     final_directory = os.getenv("UPLOAD_FILE")
    #     # file_resources_path = "File_Resources"
    #
    #     # Construct the absolute path to the file
    #     absolute_path_to_file = os.path.join(current_directory, f"{final_directory}")
    #     # print("current_directory : " ,absolute_path_to_file)
    #     print("current_directory", current_directory)
    #     self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
    #         absolute_path_to_file)
