from selenium.webdriver.common.by import By

from utils.logger import get_logger
from .base_page import BasePage

logger = get_logger(__name__)

class FormsPage(BasePage):

    XPATH_WITH_ID = "//*[@id = '{}']"
    CONTAINS_ID_XPATH = "//*[contains( @ id, '{}')]"
    GENDER_SIBLING = "//*[contains( @ id, '{}')]/following-sibling::*"
    GENDER_OPTIONS = "//*[contains(@id, '{}') and @value = '{}']"
    GENDER_SELECTION = "//label[@for='{}']"
    SUCCESSFUL_FORM_SUBMISSION_MESSAGE = "//*[contains(@id, 'example-modal-sizes-title-lg')]"

    field_name_to_id = {
        "Submit": "submit",
        "First Name": "firstName",
        "Last Name": "lastName",
        "Email": "userEmail",
        "Mobile Number": "userNumber",
        "Gender": "gender-radio",
        "Female": "gender-radio-2",
        "Male": "gender-radio-1",
        "Other": "gender-radio-3",
        "Date of Birth": "dateOfBirthInput",
        "Subjects": "subjectsInput",
        "Current Address": "currentAddress",
        "State": "react-select-3-input",
        "City": "react-select-4-input"
    }

    def __init__(self, driver):
        super().__init__(driver)

    def fill_field(self, field_name, value):
        field_id = self.field_name_to_id.get(field_name)
        if field_id:
            element = self.driver.find_element(By.ID, field_id)
            element.clear()
            element.send_keys(value)
        else:
            logger.info(f"No ID mapped for label: {field_name}")

    def get_field_value(self, field_name):
        field_id = self.field_name_to_id.get(field_name)
        if field_id:
            element = self.driver.find_element(By.ID, field_id)
            return element.get_attribute("value")
        else:
            logger.info(f"No ID mapped for label: {field_name}")
            return None


