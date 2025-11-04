import random
from helpers.generators import generate_email, generate_password, generate_ad_title, generate_ad_description, \
    generate_price


class TestData:
    # Тестовые пользователи
    EXISTING_USER = {
        "email": "davyd-vihara@gmail.com",
        "password": "Password123"
    }

    # Статические данные для объявлений
    AD_DATA = {
        "title": "Тестовое объявление",
        "description": "Описание тестового объявления",
        "price": "1000",
        "condition": "new"
    }

    # Методы для генерации динамических данных
    @staticmethod
    def generate_user_data():
        # Генерация данных нового пользователя
        return {
            "email": generate_email(),
            "password": generate_password()
        }

    @staticmethod
    def generate_ad_data():
        # Генерация данных нового объявления
        return {
            "title": generate_ad_title(),
            "description": generate_ad_description(),
            "price": generate_price(),
            "condition": random.choice(["new", "used"])
        }
