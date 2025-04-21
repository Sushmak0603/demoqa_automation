from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException

import time
import random

from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    CARD = "//*[@class = 'card mt-4 top-card']//div[@class = 'card-body']/*[text() = '{}']"
    GROUP_HEADER_MENU_LIST_EXPANDED = "//span[@class = 'group-header']//*[@class = 'header-text' and text() = '{}']/ancestor::span/following-sibling::div[@class = 'element-list collapse show']"
    GROUP_HEADER_MENU_LIST = "//*[@class = 'group-header']//*[@class = 'header-text' and text() = '{}']/ancestor::span/following-sibling::*[@class = 'element-list collapse show']//*[@class = 'text']"

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        try:
            if isinstance(locator, str):
                element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator)))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                element.click()
                logger.info(f"Clicked on element with locator: {locator}")
                time.sleep(5)
        except (TimeoutException, WebDriverException) as e:
            logger.error(f"Failed to click on element with locator: {locator}. Exception: {e}")
            raise

    def get_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
            logger.info(f"Element found using locator: {locator}")
            return element
        except TimeoutException as e:
            logger.error(f"Timeout while waiting for element with locator: {locator}. Exception: {e}")
            raise

    def get_all_elements(self, locator):
        try:
            elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            logger.info(f"Found {len(elements)} elements using locator: {locator}")
            return elements
        except TimeoutException as e:
            logger.error(f"Timeout while waiting for elements with locator: {locator}. Exception: {e}")
            raise

    def wait_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            logger.info(f"Element is visible with locator: {locator}")
            return element
        except TimeoutException as e:
            logger.error(f"Element is not visible with locator: {locator}. Exception: {e}")
            raise

    def is_visible(self, locator):
        try:
            self.wait_visible(locator)
            logger.info(f"Element is visible: {locator}")
            return True
        except Exception as e:
            logger.warning(f"Element is NOT visible: {locator}. Exception: {e}. Exception: {e}")
            return False

    def find_elements(self, by, locator, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((by, locator)))
            logger.info(f"Found {len(elements)} elements using ({by}, '{locator}')")
            return elements
        except TimeoutException as e:
            logger.error(f"Timeout while finding elements using ({by}, '{locator}'). Exception: {e}")
            raise

    def find_element(self, by, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))
            logger.info(f"Element found using ({by}, '{locator}')")
            return element
        except TimeoutException as e:
            logger.error(f"Timeout while finding element using ({by}, '{locator}'). Exception: {e}")
            raise

    def click_all_while_visible(self, visible_locator, clickable_locator):
        try:
            while self.is_visible(visible_locator):
                self.click(clickable_locator)
                logger.info(f"Clicked visible element using locator: {clickable_locator}")
        except Exception as e:
            logger.error(f"Error in click_all_while_visible with locator: {clickable_locator}. Exception: {e}")
            raise

    def get_menu_items_under_group(self, group_header_name):
        try:
            elements = self.find_elements(By.XPATH, self.GROUP_HEADER_MENU_LIST.format(group_header_name))
            texts = [el.text.strip() for el in elements if el.text.strip()]
            logger.info(f"Menu items under '{group_header_name}': {texts}")
            return texts
        except Exception as e:
            logger.error(f"Error getting menu items under group '{group_header_name}'.. Exception: {e}")
            raise

    def click_random_element(self, elements):
        try:
            if not elements:
                raise Exception("No elements to click")

            random_element = random.choice(elements)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_element)
            random_element.click()
            logger.info(f"Clicked on random element with text: '{random_element.text.strip()}'")
            return random_element
        except Exception as e:
            logger.error(f"Failed to click on a random element. Exception: {e}")
            raise

    def get_relative_element(self, element, relative_xpath):
        try:
            relative_element = element.find_element(By.XPATH, relative_xpath)
            logger.info(f"Found relative element using XPath: {relative_xpath}")
            return relative_element
        except Exception as e:
            logger.error(f"Could not find relative element using XPath '{relative_xpath}'. Exception: {e}")
            raise

    def poll_until_visible(self, locator, timeout=10, poll_frequency=1):
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
            logger.info(f"Element became visible using locator: {locator}")
            return element
        except TimeoutException as e:
            logger.error(f"Timeout while polling for element visibility using locator: {locator}. Exception: {e}")
            raise

    def fetch_value_of_css_property(self, element, property_name):
        try:
            value = element.value_of_css_property(property_name)
            logger.info(f"Fetched CSS property '{property_name}' with value: {value}")
            return value
        except Exception as e:
            logger.error(f"Failed to fetch CSS property '{property_name}'. Exception: {e}")
            raise

    def is_clickable(self, by, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
            logger.info(f"Element located by ({by}, '{locator}') is clickable.")
            return True
        except TimeoutException:
            logger.warning(f"Element located by ({by}, '{locator}') is NOT clickable within {timeout} seconds.")
            return False

