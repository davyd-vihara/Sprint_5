from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from data.test_data import TestData
from locators.main_page_locators import MainPageLocators
from config import Config


class TestLogin:
    def test_successful_login(self, driver):
        #Login пользователя
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)

        driver.get(Config.BASE_URL)
        main_page.open_login_form()

        # Заполняем форму авторизации существующим пользователем
        auth_page.login(
            TestData.EXISTING_USER["email"],
            TestData.EXISTING_USER["password"]
        )

        # Проверяем успешный логин
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.USER_NAME)
        )

        assert driver.find_element(*MainPageLocators.USER_NAME).is_displayed()
        assert driver.find_element(*MainPageLocators.LOGOUT_BUTTON).is_displayed()
        assert "User." in driver.find_element(*MainPageLocators.USER_NAME).text
