from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants
from config import URLS


def test_navigation_to_personal_account(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.PERSONAL_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PERSONAL_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.DATA_CHANGE))
    assert URLS.URL_ACCOUNT in driver.current_url

