from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from behave import given, when, then
from utils.logger import get_logger

logger = get_logger(__name__)

@then('the user navigates to "{menu_item}" section under "{group_header}"')
def step_impl(context, menu_item, group_header):
    try:
        context.page.checkbox.click(context.page.checkbox.MENU_ITEM.format(group_header, menu_item))
        logger.info(f"Navigated to '{menu_item}' under '{group_header}'")
    except Exception as e:
        logger.exception(f"Failed to navigate to '{menu_item}' under '{group_header}'")
        raise

@then('the user should be able to see "{tree_node}" in the tree node')
def step_impl(context, tree_node):
    try:
        is_visible = context.page.base.is_visible(context.page.checkbox.TREE_NODE_TEXT.format(tree_node))
        assert is_visible, f"Tree node '{tree_node}' is not visible"
        logger.info(f"Tree node '{tree_node}' is visible")
    except AssertionError as ae:
        logger.error(str(ae))
        raise
    except Exception as e:
        logger.exception(f"Error checking visibility of tree node '{tree_node}'")
        raise

@then('the user expands the tree at all levels - through code')
def step_impl(context):
    try:
        context.page.base.click_all_while_visible(context.page.checkbox.COLLAPSE_BUTTON, context.page.checkbox.COLLAPSE_BUTTON)
        logger.info("Successfully expanded all tree levels")
    except Exception as e:
        logger.exception("Error while expanding tree at all levels")
        raise

@then('the user ticks "{parent_node}" parent node in the tree')
def step_impl(context, parent_node):
    try:
        context.page.base.click(context.page.checkbox.PARENT_NODE_CHECKBOX_FOR_GIVEN_TEXT.format(parent_node))
        context.clicked_element = context.page.checkbox.PARENT_NODE_CHECKBOX_FOR_GIVEN_TEXT.format(parent_node)
        context.selected_node = parent_node
        logger.info(f"Ticked parent node '{parent_node}'")
    except Exception as e:
        logger.exception(f"Failed to tick parent node '{parent_node}'. Check if you a valid parent node is mentioned and not leaf node.")
        raise

@then('verify if all the ancestors of the selected parent node are half-ticked and fully-ticked accordingly')
def step_impl(context):
    given_node = context.selected_node
    to_be_fully_ticked = []
    to_be_half_ticked = []
    root_node = None

    try:
        while True:
            parent_node = None
            try:
                # Try finding the parent node of the current node
                parent_node_element = context.page.base.find_element(
                    By.XPATH, context.page.checkbox.PARENT_NODE_OF_GIVEN_NODE.format(given_node)
                )

                parent_node = parent_node_element.text.strip()
                if not parent_node:
                    logger.warning("Parent node element found but has no text. Breaking loop.")
                    break

                logger.info(f"Found parent node: {parent_node}")

            except TimeoutException:
                logger.info("No more parent node found. Exiting loop.")
                break
            except Exception as e:
                logger.exception("Unexpected error while finding parent node.")
                break

            # Update root_node with last valid parent for assertion later
            root_node = parent_node

            try:
                child_node_elements = context.page.base.get_all_elements(
                    context.page.checkbox.ALL_CHILDREN_OF_GIVEN_NODE.format(parent_node)
                )
            except Exception as e:
                logger.warning(f"Could not fetch child nodes for parent '{parent_node}': {e}")
                child_node_elements = []

            child_nodes = [el.text.strip() for el in child_node_elements if el.text.strip()]

            if child_nodes:
                for node in child_nodes:
                    try:
                        if context.page.base.is_visible(context.page.checkbox.IS_CHECKED.format(node)):
                            to_be_fully_ticked.append(node)
                            logger.info(f"Child node '{node}' is checked")
                        elif context.page.base.is_visible(context.page.checkbox.HALF_CHECKED.format(node)):
                            to_be_half_ticked.append(node)
                            logger.info(f"Child node '{node}' is half-checked")
                    except Exception as e:
                        logger.warning(f"Could not determine checked status for node '{node}': {e}")
            else:
                logger.info(f"No child nodes found for parent node '{parent_node}'")

            # Move up one level in the tree
            given_node = parent_node

        logger.info(f"Fully ticked nodes: {to_be_fully_ticked}")
        logger.info(f"Half ticked nodes: {to_be_half_ticked}")

        if to_be_half_ticked:
            if root_node:
                assert context.page.base.is_visible(context.page.checkbox.HALF_CHECKED.format(root_node)), \
                    f"Root node '{root_node}' is not half-ticked"
            else:
                raise AssertionError("Root node could not be determined for half-check validation")

            for node in to_be_half_ticked:
                assert context.page.base.is_visible(context.page.checkbox.HALF_CHECKED.format(node)), \
                    f"Node '{node}' is not half-checked"

        if to_be_fully_ticked:
            for node in to_be_fully_ticked:
                assert context.page.base.is_visible(context.page.checkbox.IS_CHECKED.format(node)), \
                    f"Node '{node}' is not fully-checked"

        logger.info("Ancestor tick validation successful.")

    except AssertionError as ae:
        logger.error(str(ae))
        raise
    except Exception as e:
        logger.exception(f"Error occurred while validating ancestor nodes. Exception: {e}.")
        raise


@then('verify if all the descendents of the selected parent node are fully-ticked automatically')
def step_impl(context):
    parent_node = context.selected_node
    try:
        descendent_nodes = context.page.base.get_all_elements(
            context.page.checkbox.DESCENDENT_NODES_FOR_GIVEN_PARENT_NODE.format(parent_node)
        )
        logger.info(f"Descendent nodes for '{parent_node}': {[node.text for node in descendent_nodes]}")

        for node in descendent_nodes:
            is_checked = context.page.base.is_visible(context.page.checkbox.IS_CHECKED.format(node.text))
            assert is_checked, f"Descendent node '{node.text}' is not checked"
            logger.info(f"Descendent node '{node.text}' is checked")

        logger.info("All descendant nodes are fully ticked by default.")

    except AssertionError as ae:
        logger.error(str(ae))
        raise
    except Exception as e:
        logger.exception(f"Error occurred while validating descendant nodes.. Exception: {e}")
        raise

@then('the user expands the tree at all levels - through expand all (+) button')
def step_impl(context):
    try:
        context.page.base.click(context.page.checkbox.EXPAND_ALL_BUTTON)
        logger.info("Clicked on 'Expand All' button")
    except Exception as e:
        logger.exception(f"Error occurred while clicking 'Expand All' button. Exception: {e}")
        raise