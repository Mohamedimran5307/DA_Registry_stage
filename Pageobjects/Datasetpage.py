from selenium.webdriver.common.by import By

from Configurations.config import Testdata
from Pageobjects.Basepage import Basepage

"""By locators"""


class Datasetspage(Basepage):
    DATASET_TAB = (By.ID, "navbar-dataset")
    # LIST_VIEW_BUTTON = (By.XPATH,"//p[text()='List view']")
    LIST_VIEW_BUTTON = (By.ID, "dataset-list-view-id")
    ADD_NEW_DATASET = (By.ID, "dataset-add-new-dataset-in-gridview")
    ADD_NEW_BUTTON_LIST_VIEW = (By.ID, "dataset-add-new-dataset")
    ADD_DATASET_NAME_FIELD = (By.ID, "add-dataset-name")
    Add_DATASET_DESCRIPTION_FIELD = (By.ID, "add-dataset-description")
    CONSTANTLY_UPDATING_CHECKBOX = (By.ID, "check-box-Constantly-updating")
    NEXT_BUTTON = (By.ID, "add-dataset-submit-btn")
    CANCEL_BUTTON = (By.ID, "add-dataset-cancel-btn")
    UPLOAD_LOCAL = (By.XPATH, "//input[@type='file']")
    UPLOAD_FILE = (By.ID, "add-dataset-upload-file-btn")
    DELETE_BUTTON = (By.ID, "accordion-uploaded-file-delete-button-id0")
    FILE_STANDARIZE_FIELD = (By.ID, "standardi-seselect-file-name")
    FILE_FOR_STANDARIZATION = (By.ID, "standardise-file-name-0")
    SELECT_DATAPOINT_ATTRIBUTE_STD = (By.ID, "standardise-select-datapoint-category1")
    DATAPOINT_CATEGORY = (By.ID, "standardise-datapoint-category-option-2")
    DATAPOINT_CATEGORY_2 = (By.ID, "standardise-datapoint-category-option-1")
    CLEAR_DATAPOINT_ATTRIBUTE = (By.ID, "standardise-clear-datapoint-category1")
    DATAPOINT_ATTRIBUTE_FIELD = (By.ID, "standardise-datapoint-attribute1")
    DATAPOINT_ATTRIBUTE = (By.ID, "standardise-datapoint-attribute-1")
    MASK_CHECK_BOX = (By.ID, "check-box-1")
    APPLY_BUTTON = (By.ID, "standardise-apply-btn")
    CATEGORY_ACCORDION = (By.ID, "uploaded-file-accordion-0")
    SELECT_CATEGORY = (By.ID, "check-box-0")
    SELECT_GREOGRAPHY_FIELD = (By.ID, "geography-select-country")
    SELECT_COUNTRY = (By.ID, "geography-select-countryIndia")
    SELECT_STATE_FIELD = (By.ID, "geography-select-state")
    SELECT_STATE = (By.ID, "geography-select-stateAndhra Pradesh")
    SELECT_CITY_FIELD = (By.ID, "geography-select-city")
    SELECT_CITY = (By.ID, "geography-select-cityAdoni")
    UPLOAD_POLICY_FIELD = (By.ID, "usege-policy-select-file")
    UPLOAD_POLICY_FILE = (By.ID, "usage_policy-file-name-0")
    APPLY_BUTTON_STD = (By.ID, "usege-policy-apply-btn")
    SUBMIT_BUTTON = (By.ID, "add-dataset-submit-btn")
    MySQL_TAB = (By.ID, "add-dataset-upload-type-mysql")
    DATABASE_NAME_FIELD_MySQL = (By.XPATH, "MySQL-upload-dataset-db-name-id")
    USER_NAME_MYSQL_FIELD = (By.ID, "MySQL-upload-dataset-user-name-id")
    PASSWORD_MYSQL_FIELD = (By.ID, "MySQL-upload-dataset-password-id")
    DATABASE_HOST_URL_MySQL_FIELD = (By.ID, "MySQL-upload-dataset-database-host-url-id")
    MYSQL_PORT_FIELD = (By.ID, "MySQL-upload-dataset-port-id")
    MYSQL_CONNECT_BUTTON = (By.ID, "MySQL-upload-dataset-connect-btn")
    SELECT_TABLE_MYSQL_FIELD = (By.ID, "MySQL-upload-dataset-select-id")
    SELECT_TABLE_MYSQL = (By.ID, "MySQL-upload-dataset-select-id-7")
    SELECT_COLUMN_MYSQL_1 = (By.ID, "MySQL-uploaded-data-checkbox-id-0")
    SELECT_COLUMN_MYSQL_2 = (By.ID, "MySQL-uploaded-data-checkbox-id-1")
    FILE_NAME_MYSQL_IMPORT_DATA_FIELD = (By.ID, "MySQL-upload-dataset-filename-id")
    IMPORT_BUTTON_MYSQL = (By.ID, "MySQL-upload-dataset-import-btn")
    POSTGRES_TAB = (By.ID, "add-dataset-upload-type-postgres")
    DATABASE_NAME_FIELD_Postgres = (By.ID, "Postgres-upload-dataset-db-name-id")
    USER_NAME_POSTGRES_FIELD = (By.ID, "Postgres-upload-dataset-user-name-id")
    PASSWORD_POSTGRES_FIELD = (By.ID, "Postgres-upload-dataset-password-id")
    DATABASE_HOST_URL_POSTGRES_FIELD = (By.ID, "Postgres-upload-dataset-database-host-url-id")
    POSTGRES_PORT_FIELD = (By.ID, "Postgres-upload-dataset-port-id")
    POSTGRES_CONNECT_BUTTON = (By.ID, "Postgres-upload-dataset-connect-btn")
    SELECT_TABLE_POSTGRES_FIELD = (By.ID, "Postgres-upload-dataset-select-id")
    SELECT_TABLE_POSTGRES = (By.ID, "Postgres-upload-dataset-select-id-9")
    SELECT_COLUMN_POSTGRES_1 = (By.ID, "Postgres-uploaded-data-checkbox-id-0")
    SELECT_COLUMN_POSTGRES_2 = (By.ID, "Postgres-uploaded-data-checkbox-id-1")
    FILE_NAME_POSTGRES_IMPORT_DATA_FIELD = (By.ID, "Postgres-upload-dataset-filename-id")
    IMPORT_BUTTON_POSTGRES = (By.ID, "Postgres-upload-dataset-import-btn")
    REST_API_TAB = (By.ID, "add-dataset-upload-type-rest-api")
    API_URL_FIELD = (By.ID, "upload-dataset-api-url-id")
    AUTH_TYPE_FIELD = (By.ID, "upload-dataset-api-select-auth-type-id")
    NO_AUTH_OPTION = (By.ID, "upload-dataset-api-auth-type-0")
    API_KEY_OPTION = (By.ID, "upload-dataset-api-auth-type-1")
    API_KEY_NAME_FIELD = (By.ID, "upload-dataset-api-key-id")
    KEY_KEY_VALUE_FIELD = (By.ID, "upload-dataset-api-key-value-id")
    BEARER_OPTION = (By.ID, "upload-dataset-api-auth-type-2")
    AUTH_TOKEN_FIELD = (By.ID, "upload-dataset-api-auth-token-id")
    FILE_NAME_REST_API_IMPORT_DATA_FIELD = (By.ID, "upload-dataset-api-name-of-import-file-id")
    IMPORT_REST_API_BUTTON = (By.ID, "upload-dataset-api-import-btn")
    SIGN_OUT_BUTTON = (By.ID, "navbar-signout")
    FIRST_DATASET = (By.ID, "dataset-card-view-id0")
    EDIT_DATASET = (By.XPATH, "//button[text()='Edit dataset']")
    ACCORDION_UPLOADED_FILES = (By.XPATH, "//p[text()='Uploaded Files']")
    DOWNLOAD_UPLOADED_FILES = (By.XPATH, "//button[text()='Download']")
    SECOND_DATASET = (By.ID, "dataset-card-view-id1")
    DELETE_DATASET = (By.XPATH, "//button[text()='Delete dataset']")
    CONFIRM_DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-testid=deletepopper]")
    BACK_BUTTON = (By.XPATH, "//button[text()='Back']")
    DATASETS_LOAD_MORE_BUTTON = (By.ID, "dataset-loadmore-btn")
    SEARCH_DATASET = (By.ID, "dataset-search-input-id")
    FILTER_GEOGRAPHY = (By.ID, "dataset-filter-by-geography-id")
    FILTER_COUNTRY = (By.ID, "dataset-filter-by-country-id")
    FILTER_SELECT_COUNTRY = (By.ID, "dataset-filter-country-id100")
    FILTER_STATE = (By.ID, "select-country-in-geography-id")
    FILTER_SELECT_STATE = (By.ID, "select-country-in-geography-id1")
    FILTER_SELECT_CITY = (By.ID, "select-state-in-geography-id8")  # Anantapur - No datasets
    FILTER_CITY = (By.ID, "select-state-in-geography-id")
    CANCEL_CITY = (By.CSS_SELECTOR, "svg[data-testid=CancelIcon]")
    FILTER_CATEGORY = (By.ID, "dataset-filter-by-categories-id")
    CHECKBOX_SUBCATEGORY = (By.ID, "check-box-0")
    FILTER_DATE = (By.ID, "dataset-filter-by-date-id")
    FROM_DATE_FIELD_FILTER = (By.ID, "filter-by-date-from-date")
    END_DATE_FIELD_FILTER = (By.ID, "filter-by-date-to-date")
    CLEAR_ALL_BUTTON_FILTERS = (By.ID, "dataset-filter-clear-all-id")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.BASEURL)

    def test_adding_dataset(self):
        self.do_click(self.ADD_NEW_DATASET)
        self.do_click(self.ADD_DATASET_NAME_FIELD)
        self.do_sendkeys(self.ADD_DATASET_NAME_FIELD, Testdata.CONNECTOR_NAME)
        self.do_click(self.Add_DATASET_DESCRIPTION_FIELD)
        self.do_sendkeys(self.Add_DATASET_DESCRIPTION_FIELD, Testdata.CONNECTOR_DESCRIPTION)
        self.do_click(self.CONSTANTLY_UPDATING_CHECKBOX)
        self.do_click(self.NEXT_BUTTON)
        self.do_sendkeys(self.UPLOAD_LOCAL, Testdata.UPLOAD_FILE)
        self.do_click(self.DELETE_BUTTON)
        self.do_sendkeys(self.UPLOAD_LOCAL, Testdata.UPLOAD_FILE)
        self.do_click(self.UPLOAD_FILE)
        self.do_click(self.NEXT_BUTTON)
        self.do_click(self.DELETE_BUTTON)
        self.do_sendkeys_1()
        self.do_click(self.UPLOAD_FILE)
        self.driver.execute_script("window.scrollBy(0,500);")
        self.do_click(self.NEXT_BUTTON)
        self.do_click(self.FILE_STANDARIZE_FIELD)
        self.do_click(self.FILE_FOR_STANDARIZATION)
        self.do_click(self.SELECT_DATAPOINT_ATTRIBUTE_STD)
        self.do_click(self.DATAPOINT_CATEGORY)
        self.do_click(self.CLEAR_DATAPOINT_ATTRIBUTE)
        self.do_click(self.SELECT_DATAPOINT_ATTRIBUTE_STD)
        self.do_click(self.DATAPOINT_CATEGORY)
        self.do_click(self.DATAPOINT_ATTRIBUTE_FIELD)
        self.do_click(self.DATAPOINT_ATTRIBUTE)
        self.do_clickable_mask()
        self.driver.execute_script("window.scrollBy(0,2000);")
        self.do_click(self.APPLY_BUTTON)
        self.do_click(self.NEXT_BUTTON)
        self.driver.execute_script("window.scrollBy(0,-300);")
        self.do_click(self.CATEGORY_ACCORDION)
        self.do_clickable_CATEGORY()
        self.driver.execute_script("window.scrollBy(0,600);")
        self.do_click(self.SELECT_GREOGRAPHY_FIELD)
        self.do_click(self.SELECT_COUNTRY)
        self.do_click(self.SELECT_STATE_FIELD)
        self.do_click(self.SELECT_STATE)
        self.do_click(self.SELECT_CITY_FIELD)
        self.do_click(self.SELECT_CITY)
        self.do_click(self.NEXT_BUTTON)
        self.driver.execute_script("window.scrollBy(0,-300);")
        self.do_click(self.UPLOAD_POLICY_FIELD)
        self.do_click(self.UPLOAD_POLICY_FILE)
        self.driver.execute_script("window.scrollBy(0,700);")
        self.do_clickable_REGISTER_USER()
        self.driver.execute_script("window.scrollBy(0,600);")
        self.do_click(self.APPLY_BUTTON_STD)
        self.do_click(self.SUBMIT_BUTTON)
