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
        # Works only if a parent node is selected and NOT leaf node
        if context.page.base.is_visible(context.page.checkbox.LEAF_NODE_ITEM.format(parent_node)):
            logger.error(f"'{parent_node}' is a leaf node and cannot be ticked.")
            raise AssertionError(f"'{parent_node}' is a leaf node and cannot be ticked.")
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
    to_be_fully_ticked_ancestors = []
    to_be_half_ticked_ancestors = []

    while True:
        try:
            # Try finding the parent node of the current node
            parent_node_element = context.page.base.find_element(
                By.XPATH, context.page.checkbox.PARENT_NODE_OF_GIVEN_NODE.format(given_node)
            )

            if not parent_node_element:
                logger.warning(f"Parent node element not found for '{given_node}' or we have reached the root directory. Breaking loop.")
                break

            parent_node = parent_node_element.text.strip()
            logger.info(f"Found parent node: {parent_node}")

            child_node_elements = context.page.base.get_all_elements(
                context.page.checkbox.ALL_CHILDREN_OF_GIVEN_NODE.format(parent_node)
            )

            if child_node_elements:
                if len(child_node_elements) == 1 :
                    to_be_fully_ticked_ancestors.append(parent_node)
                elif len(child_node_elements) > 1:
                    to_be_half_ticked_ancestors.append(parent_node)
            else:
                break

            given_node = parent_node

        except Exception as e:
            logger.exception(f"Unexpected error while finding parent node. Exception: {e}")
            break

    logger.info(f"To be Fully ticked ancestor nodes: {to_be_fully_ticked_ancestors} for {context.selected_node}")
    logger.info(f"To be Half ticked ancestor nodes: {to_be_half_ticked_ancestors} for {context.selected_node}")

    if to_be_half_ticked_ancestors:
        for node in to_be_half_ticked_ancestors:
            assert context.page.base.is_visible(context.page.checkbox.HALF_CHECKED.format(node)), \
                f"Node '{node}' is not half-checked"

    if to_be_fully_ticked_ancestors:
        for node in to_be_fully_ticked_ancestors:
            assert context.page.base.is_visible(context.page.checkbox.IS_CHECKED.format(node)), \
                f"Node '{node}' is not fully-checked"

@then('verify if all the descendants of the selected parent node are fully-ticked automatically')
def step_impl(context):
    selected_node = context.selected_node
    try:
        descendant_nodes = context.page.base.get_all_elements(
            context.page.checkbox.DESCENDENT_NODES_FOR_GIVEN_PARENT_NODE.format(selected_node)
        )
        logger.info(f" All Descendant nodes for '{selected_node}': {[node.text for node in descendant_nodes]}")

        for node in descendant_nodes:
            is_checked = context.page.base.is_visible(context.page.checkbox.IS_CHECKED.format(node.text))
            if is_checked:
                logger.info(f"Descendant node '{node.text}' is checked")
            assert is_checked, f"Descendant node '{node.text}' is not checked"

    except AssertionError as ae:
        logger.error(str(ae))
        raise
    except Exception as e:
        logger.exception(f"Error occurred while validating descendant nodes. Exception: {e}")
        raise

@then('the user expands the tree at all levels - through expand all (+) button')
def step_impl(context):
    try:
        context.page.base.click(context.page.checkbox.EXPAND_ALL_BUTTON)
        logger.info("Clicked on 'Expand All' button")
    except Exception as e:
        logger.exception(f"Error occurred while clicking 'Expand All' button. Exception: {e}")
        raise