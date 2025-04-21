from pages.base_page import BasePage
from pages.checkbox_page import CheckboxPage
from pages.dynamic_properties_page import DynamicPropertiesPage
from pages.book_store_page import BookStorePage
from pages.forms_page import FormsPage

class PageManager:
    def __init__(self, driver):
        self.driver = driver
        self.base = BasePage(driver)
        self.checkbox = CheckboxPage(driver)
        self.dynamic_properties = DynamicPropertiesPage(driver)
        self.book_store = BookStorePage(driver)
        self.forms = FormsPage(driver)