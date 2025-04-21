from selenium.webdriver.common.by import By
from behave import given, when, then
import time
from utils.logger import get_logger

logger = get_logger(__name__)


@when('the user clicks on "{field_name}" button')
def step_impl(context, field_name):
    logger.info(f"Attempting to click on '{field_name}' button")
    try:
        field_id = context.page.forms.field_name_to_id.get(field_name)
        context.page.base.click(context.page.forms.XPATH_WITH_ID.format(field_id))
        logger.info(f"Clicked on '{field_name}' button")
    except Exception as e:
        logger.exception(f"Failed to click on '{field_name}' button: {e}")
        raise


@then('the field "{field_name}" should indicate error with "{property}" red')
def step_impl(context, field_name, property):
    logger.info(f"Verifying red border for '{field_name}' field")
    try:
        field_id = context.page.forms.field_name_to_id.get(field_name)
        element = context.page.base.find_element(By.XPATH, context.page.forms.XPATH_WITH_ID.format(field_id))
        color = context.page.base.fetch_value_of_css_property(element, property)

        if color != 'rgb(220, 53, 69)':
            logger.error(f"Field '{field_name}' does not have red border. Current color: {color}")
        assert color == 'rgb(220, 53, 69)'
    except Exception as e:
        logger.exception(f"Border check failed for field '{field_name}': {e}")
        raise


@then('the field options for "{field_name}" should indicate error with "{property}" red')
def step_impl(context, field_name, property ):
    logger.info("Verifying red border for Gender radio options")
    field_id = context.page.forms.field_name_to_id.get(field_name)
    elements = context.page.base.find_elements(By.XPATH, context.page.forms.GENDER_SIBLING.format(field_id))
    for element in elements:
        color = context.page.base.fetch_value_of_css_property(element, property)
        if color != 'rgba(220, 53, 69, 1)':
            logger.error(f"Gender option element does not have red border. Current color: {property}")
        assert color == 'rgba(220, 53, 69, 1)'


@when('the user enters "{value}" in "{field_name}" field')
def step_impl(context, value, field_name):
    logger.info(f"Entering value '{value}' into '{field_name}' field")
    context.page.forms.fill_field(field_name, value)


@when('the user selects "{gender_selection}" gender radio button')
def step_impl(context, gender_selection):
    logger.info(f"Selecting '{gender_selection}' gender radio button")
    field_id = context.page.forms.field_name_to_id.get(gender_selection)
    context.page.base.click(context.page.forms.GENDER_SELECTION.format(field_id))
    logger.info(f"'{gender_selection}' gender selected")


@then('the form should be submitted with message "{success_message}"')
def step_impl(context, success_message):
    logger.info("Verifying form submission success message")
    try:
        message_displayed = context.page.base.find_element(By.XPATH,
                                                           context.page.forms.SUCCESSFUL_FORM_SUBMISSION_MESSAGE).text
        if message_displayed != success_message:
            logger.error(f"Form submission failed. Expected: '{success_message}' but got: '{message_displayed}'")
        assert message_displayed == success_message
    except Exception as e:
        logger.exception(f"Form submission message validation failed: {e}")
        raise


@then('verify if the "{field_name}" field has accepted only "{digit_count}" digits')
def step_impl(context, field_name, digit_count):
    logger.info(f"Validating digit count for field '{field_name}'")
    try:
        entered_value = context.page.forms.get_field_value(field_name)
        if len(entered_value) != int(digit_count):
            logger.error(f"Field '{field_name}' has {len(entered_value)} digits. Expected: {digit_count}")
        assert len(entered_value) == int(digit_count)
    except Exception as e:
        logger.exception(f"Digit count validation failed for '{field_name}': {e}")
        raise
