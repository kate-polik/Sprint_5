from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from generators import DataInput
from constants import Constants


def navigate_to_registration_page(driver):
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.REGISTRATION_BUTTON)).click()


def fill_registration_form(driver, email, password):
    driver.find_element(*Locators.NAME_INPUT).send_keys(email)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)


# Тест: успешная регистрация
def test_successful_registration(driver):
    navigate_to_registration_page(driver)
    fill_registration_form(driver, DataInput.email, DataInput.password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    assert WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Locators.PAGE_INPUT))


# Тест: ошибка регистрации с коротким паролем
def test_registration_error_short_password(driver):
    navigate_to_registration_page(driver)
    fill_registration_form(driver, DataInput.email, Constants.INVALID_PASSWORD)
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    error_message = driver.find_element(*Locators.ERROR_MESSAGE).text
    assert "Некорректный пароль" in error_message, "Ожидаемое сообщение об ошибке отсутствует."
