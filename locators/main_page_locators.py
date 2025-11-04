from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
