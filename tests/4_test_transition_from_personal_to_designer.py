from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants
from config import URLS


# Функция для входа в личный кабинет
def login_to_account(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.PERSONAL_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PERSONAL_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()


# Тест: Переход из личного кабинета в конструктор по клику на "Конструктор"
def test_navigate_to_constructor_from_personal_account_via_constructor_button(driver):
    login_to_account(driver)
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    assert URLS.URL in driver.current_url
    assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.BUTTON_ORDER))


# Тест: Переход из личного кабинета в конструктор по клику на логотип
def test_navigate_to_constructor_from_personal_account_via_logo(driver):
    login_to_account(driver)
    driver.find_element(*Locators.LOGO_BUTTON).click()
    assert URLS.URL in driver.current_url
    assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.BUTTON_ORDER))
