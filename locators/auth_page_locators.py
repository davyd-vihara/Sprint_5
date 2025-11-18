from selenium.webdriver.common.by import By


class AuthPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//button[contains(text(), 'Забыли пароль?')]")
    ALREADY_HAVE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Уже есть аккаунт')]")
    ERROR_FIELD = (By.XPATH, "//*[contains(text(), 'Ошибка')]")
