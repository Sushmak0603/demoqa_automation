from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException

from utils.logger import get_logger

logger = get_logger(__name__)

@given('the user has launched the DEMOQA application')
def step_impl(context):
    try:
        context.driver.get(context.base_url)
        logger.info("Launched DEMOQA application")
    except WebDriverException as e:
        logger.error(f"Failed to launch DEMOQA application: {e}")
        raise

@given('the user click on "{card_name}" card')
def step_impl(context, card_name):
    try:
        context.page.base.click(context.page.base.CARD.format(card_name))
        logger.info(f"Clicked on '{card_name}' card")
    except Exception as e:
        logger.error(f"Failed to click on '{card_name}' card: {e}")
        raise

@then('the user should be navigated to a URL containing "{expected_path}"')
def step_impl(context, expected_path):
    try:
        WebDriverWait(context.driver, 10).until(
            lambda driver: expected_path in driver.current_url
        )
        current_url = context.driver.current_url
        logger.info(f"Navigation successful. Current URL: {current_url}")
        assert expected_path in current_url, f"Expected '{expected_path}' in URL, but got: {current_url}"
    except TimeoutException:
        logger.error(f"Timeout: '{expected_path}' not found in the URL within the wait time")
        raise
    except AssertionError as ae:
        logger.error(str(ae))
        raise

@then('the menu list for "{group_header_name}" should be expanded')
def step_impl(context, group_header_name):
    try:
        is_expanded = context.page.base.is_visible(
            context.page.base.GROUP_HEADER_MENU_LIST_EXPANDED.format(group_header_name)
        )
        logger.info(f"Menu list expanded check for '{group_header_name}': {is_expanded}")
        assert is_expanded, f"Menu list for group header '{group_header_name}' is not expanded"
    except AssertionError as ae:
        logger.error(str(ae))
        raise
    except Exception as e:
        logger.error(f"Error while checking if menu list is expanded for '{group_header_name}': {e}")
        raise

@then('the menu list items for "{group_header}" should be')
def step_impl(context, group_header):
    try:
        expected_items = [row[0].strip() for row in context.table]
        actual_items = context.page.base.get_menu_items_under_group(group_header)

        logger.info(f"Expected menu items for '{group_header}': {expected_items}")
        logger.info(f"Actual menu items: {actual_items}")

        for expected in expected_items:
            assert expected in actual_items, f"'{expected}' not found in actual menu items"

        assert len(expected_items) == len(actual_items), "Menu item count mismatch"
        logger.info("Menu item validation successful")
    except AssertionError as ae:
        logger.error(str(ae))
        raise
    except Exception as e:
        logger.error(f"Error validating menu items for '{group_header}': {e}")
        raise

@given('the user refreshes the page')
def step_impl(context):
    try:
        context.driver.refresh()
        logger.info("Page refreshed successfully")
    except Exception as e:
        logger.error(f"Failed to refresh the page: {e}")
        raise