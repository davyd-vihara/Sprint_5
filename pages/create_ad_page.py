from .base_page import BasePage
from locators.create_ad_locators import CreateAdLocators


class CreateAdPage(BasePage):
    def create_ad(self, title, description, price, condition="new"):
        self.input_text(CreateAdLocators.TITLE_INPUT, title)
        self.input_text(CreateAdLocators.DESCRIPTION_INPUT, description)
        self.input_text(CreateAdLocators.PRICE_INPUT, price)

        if condition == "new":
            self.click(CreateAdLocators.CONDITION_NEW)
        else:
            self.click(CreateAdLocators.CONDITION_USED)

        self.click(CreateAdLocators.PUBLISH_BUTTON)

    def is_auth_modal_visible(self):
        # Проверяет модальное окно авторизации для неавторизованных
        try:
            return self.wait_for_element_visible(CreateAdLocators.AUTH_MODAL).is_displayed()
        except:
            return False
