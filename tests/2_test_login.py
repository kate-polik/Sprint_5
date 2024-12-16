from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants


def perform_login(driver, email, password):
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.BUTTON_ORDER))


# Тест для проверки входа через кнопку "Войти" на главной странице
def test_login_from_main_page(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.MAIN_LOGIN_BUTTON)).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    assert perform_login(driver, Constants.PERSONAL_EMAIL, Constants.PERSONAL_PASSWORD)


# Тест для проверки входа через кнопку «Личный кабинет»
def test_login_from_personal_account_button(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    assert perform_login(driver, Constants.PERSONAL_EMAIL, Constants.PERSONAL_PASSWORD)


# Тест для проверки входа через кнопку в форме регистрации
def test_login_from_registration_form(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.REGISTRATION_BUTTON)).click()
    driver.find_element(*Locators.REGISTRATION_LOGIN_BUTTON).click()
    assert perform_login(driver, Constants.PERSONAL_EMAIL, Constants.PERSONAL_PASSWORD)


# Тест для проверки входа через кнопку в форме восстановления пароля
def test_login_from_password_recovery_form(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.RECOVER_PASSWORD_BUTTON)).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.RECOVER_PASSWORD_LOGIN_BUTTON)).click()
    assert perform_login(driver, Constants.PERSONAL_EMAIL, Constants.PERSONAL_PASSWORD)
