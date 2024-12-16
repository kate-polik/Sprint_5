from locators import Locators


def verify_tab_state(driver, locator, expected_active):
    element = driver.find_element(*locator)
    class_attribute = element.get_attribute("class")
    if expected_active:
        assert "tab_tab_type_current__2BEPc" in class_attribute
    else:
        assert "tab_tab_type_current__2BEPc" not in class_attribute


# Тест: переход к разделу "Соусы"
def test_navigate_to_sauces_section(driver):
    driver.find_element(*Locators.SAUCE_SECTION).click()
    verify_tab_state(driver, Locators.SAUCE_ACTIVE_BUN_SECTION, expected_active=False)
    verify_tab_state(driver, Locators.SAUCE_ACTIVE_SAUCE_SECTION, expected_active=True)
    verify_tab_state(driver, Locators.SAUCE_ACTIVE_FILLING_SECTION, expected_active=False)


# Тест: переход к разделу "Начинки"
def test_navigate_to_fillings_section(driver):
    driver.find_element(*Locators.FILLING_SECTION).click()
    verify_tab_state(driver, Locators.SAUCE_ACTIVE_BUN_SECTION, expected_active=False)
    verify_tab_state(driver, Locators.SAUCE_ACTIVE_SAUCE_SECTION, expected_active=False)
    verify_tab_state(driver, Locators.SAUCE_ACTIVE_FILLING_SECTION, expected_active=True)


# Тест: переход к разделу "Булки"
def test_navigate_to_buns_section(driver):
    driver.find_element(*Locators.FILLING_SECTION).click()
    driver.find_element(*Locators.BUN_SECTION).click()
    verify_tab_state(driver, Locators.SAUCE_ACTIVE_BUN_SECTION, expected_active=True)
    verify_tab_state(driver, Locators.SAUCE_ACTIVE_SAUCE_SECTION, expected_active=False)
    verify_tab_state(driver, Locators.SAUCE_ACTIVE_FILLING_SECTION, expected_active=False)
