from .base_page import BasePage
from locators.auth_page_locators import AuthPageLocators


class AuthPage(BasePage):
    def go_to_registration(self):
        self.click(AuthPageLocators.NO_ACCOUNT_BUTTON)

    def register(self, email, password, confirm_password=None):
        if confirm_password is None:
            confirm_password = password

        self.input_text(AuthPageLocators.EMAIL_INPUT, email)
        self.input_text(AuthPageLocators.PASSWORD_INPUT, password)
        self.input_text(AuthPageLocators.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click(AuthPageLocators.CREATE_ACCOUNT_BUTTON)

    def login(self, email, password):
        self.input_text(AuthPageLocators.EMAIL_INPUT, email)
        self.input_text(AuthPageLocators.PASSWORD_INPUT, password)
        self.click(AuthPageLocators.LOGIN_BUTTON)

    def is_error_displayed(self):
        try:
            return self.wait_for_element_visible(AuthPageLocators.ERROR_FIELD).is_displayed()
        except:
            return False
