from selenium.webdriver.common.by import By

from Configurations.config import Testdata
from Pageobjects.Basepage import Basepage


class Support_Ticket_Page(Basepage):
    SUPPORT_TICKET_ICON = (By.ID, "click-support-icon")
    COSTEWARD_TICKETS = (By.ID,"Co-Steward Tickets0")
    PARTICIPANT_TICKET = (By.ID,"Participant Tickets1")
    SUPPORT_TICKET_SEARCH_INPUT_FIELD = (By.ID,"dataset-search-input-id")
    STATUS_FILTER_BUTTON = (By.ID,"status_filter")
    STATUS_OPEN_CHECKBOX = (By.ID,"open")
    STATUS_CLOSE_CHECKBOX = (By.ID,"closed")
    STATUS_CLOSE_BUTTON =(By.ID,"status-close-filter-id")
    CATEGORY_FILTER_BUTTON = (By.ID,"support-filter-by-categories-id")
    CATGEORY_FILTER_DATASETS_CHECKBOX = (By.ID,"datasets")
    CATGEORY_FILTER_CONNECTOR_CHECKBOX = (By.ID,"connectors")
    CATEGORY_CLOSE_BUTTON = (By.ID,"category-close-filter-id")
    BY_DATE_FILTER = (By.ID,"support-filter-by-date-id")
    BY_DATE_FILTER_START_DATE = (By.ID,"filter-by-date-from-date")
    BY_DATE_FILTER_END_DATE = (By.ID,"filter-by-date-to-date")
    BY_DATE_CLOSE_BUTTON = (By.ID,"date-filter-close-btn-id")
    CLEAR_ALL_BUTTON = (By.ID,"dataset-filter-clear-all-id")
    COSTEWARD_LIST_VIEW = (By.ID,"dataset-list-view-id")
    SIGN_OUT_BUTTON = (By.ID,"navbar-signout")
    LOAD_MORE_BUTTON = (By.XPATH,"//button[text()='Load more']")


    def __init__(self, driver):
        super().__init__(driver)
