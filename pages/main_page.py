from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def open_login_form(self):
        self.click(MainPageLocators.LOGIN_REGISTER_BUTTON)

    def open_create_ad(self):
        self.click(MainPageLocators.CREATE_AD_BUTTON)

    def logout(self):
        self.click(MainPageLocators.LOGOUT_BUTTON)

    def is_user_logged_in(self):
        try:
            return self.wait_for_element_visible(MainPageLocators.LOGOUT_BUTTON).is_displayed()
        except:
            return False

    def get_username(self):
        return self.wait_for_element_visible(MainPageLocators.USER_NAME).text
