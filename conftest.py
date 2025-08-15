import allure
import os
import pytest
import shutil
import stat
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver: webdriver.Remote

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action = "store",
        default = "false",
        help = "Run browser tests in headless mode"
    )

@pytest.fixture(scope="session")
def browser_headless(pytestconfig):
    headless = pytestconfig.getoption("--headless")

    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(1)

    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def google_driver():
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,
        options=options)
    
    driver.maximize_window()
    driver.get("https://google.com/")

    WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    #Time to solve google captcha
    time.sleep(30)

    yield driver

@pytest.fixture
def reset_google_page(google_driver):
    #Reset the page before each dataset on @pytest.mark.parametrize
    google_driver.get("https://google.com/")
    WebDriverWait(google_driver, 5).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    google_search_box = google_driver.find_element(By.NAME, "q")
    google_search_box.clear()

    yield google_driver