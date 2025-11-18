from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from data.test_data import TestData
from locators.main_page_locators import MainPageLocators
from config import Config


class TestLogout:
    def test_successful_logout(self, driver):
        # Logout пользователя
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        # Сначала логинимся
        driver.get(Config.BASE_URL)
        main_page.open_login_form()
        auth_page.login(
            TestData.EXISTING_USER["email"],
            TestData.EXISTING_USER["password"]
        )

        # Проверяем что залогинены
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.LOGOUT_BUTTON)
        )

        # Затем разлогиниваемся
        main_page.logout()

        # Проверяем что вышли (появилась кнопка входа)
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON)
        )

        assert driver.find_element(*MainPageLocators.LOGIN_REGISTER_BUTTON).is_displayed()
        # Проверяем что кнопка выхода исчезла
        logout_buttons = driver.find_elements(*MainPageLocators.LOGOUT_BUTTON)
        assert len(logout_buttons) == 0
