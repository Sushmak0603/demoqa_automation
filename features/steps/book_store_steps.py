from selenium.webdriver.common.by import By
from behave import given, when, then
import requests
from utils.logger import get_logger

logger = get_logger(__name__)

@then('the user fetches the books details displayed')
def step_impl(context):
    book_details_displayed = {}
    try:
        total_pages_count = int(context.page.base.get_element(context.page.book_store.TOTAL_PAGES).text.strip())
        logger.info(f"Total pages found: {total_pages_count}")

        current_page_count_element = context.page.base.find_element(By.XPATH, context.page.book_store.CURRENT_PAGE)
        current_page_count = int(current_page_count_element.get_attribute("value").strip())

        while current_page_count <= total_pages_count:
            total_rows = context.page.base.get_all_elements(context.page.book_store.ROW_GROUP)

            for i in range(len(total_rows)):
                index = i + 1  # XPath starts at 1
                row = total_rows[i]
                if not row.text.strip():
                    break

                book_title = context.page.base.driver.find_element(
                    By.XPATH, context.page.book_store.BOOK_TITLE.format(index)).text.strip()

                book_author = context.page.base.driver.find_element(
                    By.XPATH, context.page.book_store.BOOK_AUTHOR.format(index)).text.strip()

                book_publisher = context.page.base.driver.find_element(
                    By.XPATH, context.page.book_store.BOOK_PUBLISHER.format(index)).text.strip()

                book_details_displayed[book_title] = {
                    'title': book_title,
                    'author': book_author,
                    'publisher': book_publisher
                }

            logger.info(f"Fetched book details from page {current_page_count}")

            if current_page_count == total_pages_count:
                break
            elif current_page_count < total_pages_count:
                assert context.page.base.is_clickable(By.XPATH, context.page.book_store.NEXT_PAGE), \
                    "Next page button is not clickable"
                context.page.base.click(context.page.book_store.NEXT_PAGE)
                current_page_count += 1

        context.book_details_displayed = book_details_displayed
        logger.info(f"All book details fetched successfully.")

    except Exception as e:
        logger.exception(f"Exception occurred while fetching book details from UI. Exception: {e}")
        raise

@then('check if Book Store API is available')
def step_impl(context):
    try:
        url = f"{context.base_url}{context.page.book_store.BOOKS_API}"
        logger.info(f"Sending GET request to {url}")
        response = requests.get(url, verify=False)
        assert response.status_code == 200, f"Bookstore API is not available. Status code: {response.status_code}"
        logger.info("Bookstore API is available and responded with 200")

    except Exception as e:
        logger.exception(f"Exception while checking Book Store API availability. Exception: {e}")
        raise

@then('send a GET request to endpoint "{endpoint}" and fetch response')
def step_impl(context, endpoint):
    try:
        url = f"{context.base_url}{endpoint}"
        logger.info(f"Sending GET request to endpoint: {url}")
        context.response = requests.get(url, verify=False)
        logger.info(f"Received response with status code: {context.response.status_code}")
    except Exception as e:
        logger.exception(f"Exception while sending GET request to endpoint.. Exception: {e}")
        raise

@then('parse the book details from the response')
def step_impl(context):
    book_details_from_api = {}
    try:
        if context.response.status_code == 200:
            books = context.response.json().get('books', [])
            for book in books:
                book_details_from_api[book['title']] = {
                    'title': book['title'],
                    'author': book['author'],
                    'publisher': book['publisher']
                }
            logger.info(f"Book details parsed from API response: {book_details_from_api}")
        else:
            logger.error(f"Failed to fetch books from API. Status code: {context.response.status_code}")

        context.book_details_from_api = book_details_from_api
    except Exception as e:
        logger.exception(f"Exception while parsing book details from API response. Exception: {e}")
        raise

@then('compare the books details displayed with the book details fetched through API')
def step_impl(context):
    try:
        result = context.page.book_store.compare_book_details(
            context.book_details_displayed, context.book_details_from_api
        )
        assert result, "Book details do not match"
        logger.info("Book details from UI and API match successfully.")
    except AssertionError as e:
        logger.error("Mismatch between UI and API book details.")
        raise
    except Exception as e:
        logger.exception(f"Exception occurred while comparing book details. Exception: {e}")
        raise

@then('the user selects "{rows}" in the row per page dropdown')
def step_impl(context, rows):
    try:
        logger.info(f"Selecting {rows} rows per page")
        dropdown_element = context.page.base.find_element(By.XPATH, context.page.book_store.ROWS_PER_PAGE)
        context.page.book_store.select_rows_per_page(dropdown_element, rows)
        logger.info("Row selection from dropdown successful")
    except Exception as e:
        logger.exception(f"Failed to select {rows} in row per page dropdown. Exception: {e}")
        raise
