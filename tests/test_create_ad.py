from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.create_ad_page import CreateAdPage
from data.test_data import TestData
from locators.create_ad_locators import CreateAdLocators
from locators.main_page_locators import MainPageLocators
from config import Config


class TestCreateAd:
    def test_create_ad_unauthorized(self, driver):
        # Создание объявления неавторизованным пользователем
        main_page = MainPage(driver)
        create_ad_page = CreateAdPage(driver)

        driver.get(Config.BASE_URL)
        main_page.open_create_ad()

        # Проверяем что появилось модальное окно авторизации
        assert create_ad_page.is_auth_modal_visible()

    def test_create_ad_authorized(self, driver):
        # Создание объявления авторизованным пользователем
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)
        create_ad_page = CreateAdPage(driver)

        # Логинимся
        driver.get(Config.BASE_URL)
        main_page.open_login_form()
        auth_page.login(
            TestData.EXISTING_USER["email"],
            TestData.EXISTING_USER["password"]
        )

        # Ждем пока пользователь залогинится
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.presence_of_element_located(MainPageLocators.LOGOUT_BUTTON)
        )

        # Создаем объявление
        main_page.open_create_ad()

        # Ждем загрузки формы создания объявления
        WebDriverWait(driver, Config.TIMEOUT).until(
            EC.presence_of_element_located(CreateAdLocators.TITLE_INPUT)
        )

        # Используем генератор для создания уникальных данных объявления
        ad_data = TestData.generate_ad_data()

        create_ad_page.input_text(CreateAdLocators.TITLE_INPUT, ad_data["title"])
        create_ad_page.input_text(CreateAdLocators.DESCRIPTION_INPUT, ad_data["description"])
        create_ad_page.input_text(CreateAdLocators.PRICE_INPUT, ad_data["price"])

        # Публикуем (состояние оставляем по умолчанию - "Новый")
        create_ad_page.click(CreateAdLocators.PUBLISH_BUTTON)

        # Выбор категории и города (если элементы есть на форме)
        try:
            create_ad_page.click(CreateAdLocators.CATEGORY_DROPDOWN)
            create_ad_page.click(CreateAdLocators.CATEGORY_OPTION_BOOKS)
        except:
            pass  # Пропускаем если элементы не найдены

        try:
            create_ad_page.click(CreateAdLocators.CITY_DROPDOWN)
            create_ad_page.click(CreateAdLocators.CITY_OPTION_KAZAN)
        except:
            pass  # Пропускаем если элементы не найдены