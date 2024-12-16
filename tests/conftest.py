import pytest
from selenium import webdriver
from config import URLS


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URLS.URL)
    yield driver
    driver.quit()
