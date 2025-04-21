from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from utils.page_manager import PageManager
from utils.logger import get_logger

logger = get_logger(__name__)

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    context.page = PageManager(context.driver)
    context.base_url = "https://demoqa.com/"

def before_scenario(context, scenario):
    logger.info(f"Starting Scenario: {scenario.name}")

def after_scenario(context, scenario):
    if scenario.status == "passed":
        logger.info(f"Scenario Passed: {scenario.name}")
    elif scenario.status == "failed":
        logger.error(f"Scenario Failed: {scenario.name}")
def after_all(context):
    context.driver.quit()
