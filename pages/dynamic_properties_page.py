from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from utils.logger import get_logger
from .base_page import BasePage

logger = get_logger(__name__)

class DynamicPropertiesPage(BasePage):
    VISIBLE_AFTER_5_SECONDS_BUTTON = "//*[@id = 'visibleAfter']"
    COLOR_CHANGE_BUTTON = "//*[@id = 'colorChange']"

    def __init__(self, driver):
        super().__init__(driver)

    def poll_until_color_changes(self, locator, css_property, initial_value=None):
        try:
            logger.info(
                f"Waiting for CSS property '{css_property}' of element located by '{locator}' to change from '{initial_value}'")

            WebDriverWait(self.driver, timeout=10, poll_frequency=0.5).until(
                lambda d: d.find_element(By.XPATH, locator).value_of_css_property(css_property) != initial_value
            )

            new_value = self.driver.find_element(By.XPATH, locator).value_of_css_property(css_property)
            logger.info(f"CSS property '{css_property}' changed successfully from '{initial_value}' to '{new_value}'")

        except Exception as e:
            logger.exception(f"Failed to detect change in CSS property '{css_property}' for element: {locator}. Exception: {e}")
            raise

