from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from data.test_data import TestData
from locators.main_page_locators import MainPageLocators
from locators.auth_page_locators import AuthPageLocators
from config import Config


class TestRegistration:
    def test_successful_registration(self, driver):
        # Регистрация пользователя - позитивный сценарий
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        driver.get(Config.BASE_URL)
        main_page.open_login_form()
        auth_page.go_to_registration()

        # Используем генератор для создания уникальных данных
        user_data = TestData.generate_user_data()
        auth_page.register(user_data["email"], user_data["password"])

        # Проверяем успешную регистрацию
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.USER_NAME)
        )

        assert driver.find_element(*MainPageLocators.USER_NAME).is_displayed()
        assert driver.find_element(*MainPageLocators.LOGOUT_BUTTON).is_displayed()

    def test_registration_invalid_email(self, driver):
        # Регистрация с email не по маске
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        driver.get(Config.BASE_URL)
        main_page.open_login_form()
        auth_page.go_to_registration()

        # Заполняем только email (невалидный)
        auth_page.input_text(AuthPageLocators.EMAIL_INPUT, "invalid-email")
        auth_page.click(AuthPageLocators.CREATE_ACCOUNT_BUTTON)

        # Проверяем что остались на странице регистрации (не перешли)
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.presence_of_element_located(AuthPageLocators.CREATE_ACCOUNT_BUTTON)
        )
        assert "regiatration" in driver.current_url

    def test_registration_existing_user(self, driver):
        # Регистрация уже существующего пользователя
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        driver.get(Config.BASE_URL)
        main_page.open_login_form()
        auth_page.go_to_registration()

        # Используем существующие данные из test_data.py
        auth_page.register(
            TestData.EXISTING_USER["email"],
            TestData.EXISTING_USER["password"]
        )

        # Проверяем что остались на странице регистрации (не перешли на главную)
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.presence_of_element_located(AuthPageLocators.CREATE_ACCOUNT_BUTTON)
        )
        assert "regiatration" in driver.current_url
