from selenium.webdriver.common.by import By

from Configurations.config import Testdata
from Pageobjects.Basepage import Basepage


class Support_Ticket_Page(Basepage):
    SUPPORT_TICKET_ICON = (By.ID, "click-support-icon")

    def __init__(self, driver):
        super().__init__(driver)
