from selenium.webdriver.common.by import By


class CreateAdLocators:
    # Основные поля
    TITLE_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "(//textarea[@name='description'])[1]")
    PRICE_INPUT = (By.NAME, "price")

    # Радио-кнопки состояния товара
    CONDITION_NEW = (By.XPATH, "//input[@name='condition' and @value='Новый']")
    CONDITION_USED = (By.XPATH, "//input[@name='condition' and @value='Б/У']")

    # Кнопка публикации
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")

    # Модальное окно для неавторизованных
    AUTH_MODAL = (By.XPATH, "//*[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")

    # Селекторы для category и city
    CATEGORY_DROPDOWN = (By.XPATH, "//button[contains(@class,'category-dropdown')]")
    CATEGORY_OPTION_BOOKS = (By.XPATH, "//span[text()='Книги']")
    CITY_DROPDOWN = (By.XPATH, "//button[contains(@class,'city-dropdown')]")
    CITY_OPTION_KAZAN = (By.XPATH, "//span[text()='Казань']")
