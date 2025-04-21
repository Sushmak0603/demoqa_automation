from selenium.webdriver.common.by import By
from behave import given, when, then
from utils.logger import get_logger

logger = get_logger(__name__)


@then('the user fluently waits for the button with text "Visible after 5 seconds" to be displayed')
def step_impl(context):
    logger.info("Waiting for the 'Visible after 5 seconds' button to become visible...")
    try:
        locator = context.page.dynamic_properties.VISIBLE_AFTER_5_SECONDS_BUTTON
        visible_button = context.page.base.poll_until_visible(locator)
        assert visible_button.is_displayed(), "Button with text 'Visible after 5 seconds' is not displayed"
        logger.info("'Visible after 5 seconds' button is now visible.")
    except Exception as e:
        logger.exception(f"Error waiting for 'Visible after 5 seconds' button: {e}")
        raise


@given('the user fetches initial "{property}" of the button from css property')
def step_impl(context, property):
    logger.info(f"Fetching initial CSS property '{property}' of the color-change button.")
    try:
        change_color_button = context.page.base.find_element(By.XPATH, context.page.dynamic_properties.COLOR_CHANGE_BUTTON)
        context.initial_color = context.page.base.fetch_value_of_css_property(change_color_button, property)
        logger.info(f"Initial '{property}' value: {context.initial_color}")
    except Exception as e:
        logger.exception(f"Error fetching initial CSS property '{property}': {e}")
        raise


@given('the user polls to wait until the button color changes')
def step_impl(context):
    logger.info("Polling until the button color changes...")
    try:
        context.page.dynamic_properties.poll_until_color_changes(
            context.page.dynamic_properties.COLOR_CHANGE_BUTTON,
            'color',
            context.initial_color
        )
        logger.info("Button color has changed.")
    except Exception as e:
        logger.exception(f"Error while polling for button color change. Exception: {e}")
        raise


@given('the user fetches changed "{property}" of the button from css property')
def step_impl(context, property):
    logger.info(f"Fetching changed CSS property '{property}' of the color-change button.")
    try:
        change_color_button = context.page.base.find_element(By.XPATH, context.page.dynamic_properties.COLOR_CHANGE_BUTTON)
        context.changed_color = context.page.base.fetch_value_of_css_property(change_color_button, property)
        logger.info(f"Changed '{property}' value: {context.changed_color}")
    except Exception as e:
        logger.exception(f"Error fetching changed CSS property '{property}': {e}")
        raise

@then('the user asserts if the color of the button has changed')
def step_impl(context):
    logger.info(f"Aseerting if teh color of teh button has changed.")
    try:
        assert context.initial_color != context.changed_color, logger.error(f"Button color did not change. Initial: {context.initial_color}, Changed: {context.changed_color}")
        logger.info("Button color has changed successfully.")
    except:
        logger.exception("Error while asserting button color change.")
        raise