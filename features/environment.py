from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from utils.page_manager import PageManager

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    context.page = PageManager(context.driver)
    context.base_url = "https://demoqa.com/"

def after_all(context):
    context.driver.quit()
