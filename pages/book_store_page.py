from .base_page import BasePage
from selenium.webdriver.support.ui import Select

from utils.logger import get_logger

logger = get_logger(__name__)

class BookStorePage(BasePage):

    # XPATHS
    TOTAL_PAGES = "//*[@class = '-totalPages']"
    CURRENT_PAGE = "//*[@class = '-pageJump']/input[@aria-label='jump to page']"
    ROW_GROUP = "//*[@class = 'rt-tr-group']"
    BOOK_TITLE = "(//a[contains(@href, 'books')])[{}]"
    BOOK_AUTHOR = "(//a[contains(@href, 'books')]/ancestor::*[@class = 'rt-td'][1]/following-sibling::div[1])[{}]"
    BOOK_PUBLISHER = "(//a[contains(@href, 'books')]/ancestor::*[@class = 'rt-td'][1]/following-sibling::div[2])[{}]"
    NEXT_PAGE = "//*[@class = '-btn' and text() = 'Next']"
    ROWS_PER_PAGE = "//select[@aria-label = 'rows per page']"

    # API ENDPOINT
    BOOKS_API = "/BookStore/v1/Books"

    def __init__(self, driver):
        super().__init__(driver)

    from utils.logger import get_logger

    logger = get_logger(__name__)

    def compare_book_details(self, actual_dict, expected_dict):
        logger.info("Starting comparison of book details between UI and API...")
        match_status = True  # Assume everything matches unless proven otherwise

        try:
            for book_title, expected_details in expected_dict.items():
                if book_title not in actual_dict:
                    logger.error(f"[Missing Book] Book '{book_title}' not found in actual results.")
                    match_status = False
                    continue

                actual_details = actual_dict[book_title]

                actual_author = actual_details['author']
                expected_author = expected_details['author']
                actual_publisher = actual_details['publisher']
                expected_publisher = expected_details['publisher']

                logger.info(f"Comparing details for book: '{book_title}'")
                logger.info(f"Expected vs Actual Author: {expected_author} | {actual_author}")
                logger.info(f"Expected vs Actual Publisher: {expected_publisher} | {actual_publisher}")

                if actual_author != expected_author:
                    logger.error(
                        f"[Author Mismatch] Book: '{book_title}' | Expected: '{expected_author}' | Actual: '{actual_author}'")
                    match_status = False

                if actual_publisher != expected_publisher:
                    logger.error(
                        f"[Publisher Mismatch] Book: '{book_title}' | Expected: '{expected_publisher}' | Actual: '{actual_publisher}'")
                    match_status = False

            if match_status:
                logger.info("All book details matched successfully between UI and API.")
            else:
                logger.warning("Some book details did not match. Check error logs above.")

            return match_status

        except Exception as e:
            logger.exception("Exception occurred during comparison of book details.. Exception: {e}")
            return False

    def select_rows_per_page(self, dropdown_element, rows):
        try:
            select = Select(dropdown_element)
            select.select_by_value(str(rows))
            logger.info(f"Selected {rows} rows per page from dropdown.")
        except Exception as e:
            logger.error(f"Failed to select rows per page. Exception: {e}")
            raise







