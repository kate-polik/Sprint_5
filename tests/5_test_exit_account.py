from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants
from config import URLS


# Тест: Переход из личного кабинета в конструктор по клику на "Конструктор"
def test_navigate_to_constructor_from_personal_account_via_constructor_button(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.PERSONAL_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PERSONAL_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.EXIT_BUTTON)).click()
    assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.PAGE_INPUT))
    assert URLS.URL_LOGIN in driver.current_url

