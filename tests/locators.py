from selenium.webdriver.common.by import By


class Locators:
    # Главная страница
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  # Кнопка "Личный кабинет"
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    BUN_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]")  # Раздел "Булки"
    SAUCE_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]")  # Раздел "Соусы"
    FILLING_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]")  # Раздел "Начинки"
    SAUCE_ACTIVE_BUN_SECTION = (By.XPATH,
                                "//div[contains(@class, 'tab_tab__1SPyG') and .//span[contains(text(), 'Булки')]]")  # Раздел "Булки" не активен
    SAUCE_ACTIVE_SAUCE_SECTION = (By.XPATH,
                                  "//div[contains(@class, 'tab_tab__1SPyG') and .//span[contains(text(), 'Соусы')]]")  # Раздел "Соусы" активен
    SAUCE_ACTIVE_FILLING_SECTION = (By.XPATH,
                                    "//div[contains(@class, 'tab_tab__1SPyG') and .//span[contains(text(), 'Начинки')]]")  # Раздел "Начинки" не активен

    # Регистрация
    REGISTRATION_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться"
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']")  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")  # Сообщение об ошибке
    REGISTRATION_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]")  # Кнопка "Войти"

    # Вход
    PAGE_INPUT = (By.XPATH, "//h2[contains(text(),'Вход')]")  # Надпись "Вход" на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")  # Кнопка "Войти в аккаунт"
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")  # Кнопка "Восстановить пароль"

    # Авторизованный пользователь
    BUTTON_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  # Кнопка "Оформить заказ"

    # Восстановление пароля
    RECOVER_PASSWORD_LOGIN_BUTTON = (
    By.XPATH, "//a[contains(text(),'Войти')]")  # Кнопка "Войти" на странице "Восстановление пароля"

    # Личный кабинет
    DATA_CHANGE = (By.XPATH,
                   "//p[contains(text(),'В этом разделе вы можете изменить свои персональные данные')]")  # Надпись об изменении данных
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]")  # Логотип сайта
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода
