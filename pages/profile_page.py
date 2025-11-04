from .base_page import BasePage
from locators.profile_locators import ProfileLocators


class ProfilePage(BasePage):
    def get_ads_count(self):
        try:
            ads = self.driver.find_elements(*ProfileLocators.AD_ITEM)
            return len(ads)
        except:
            return 0

    def get_first_ad_title(self):
        try:
            return self.wait_for_element_visible(ProfileLocators.AD_TITLE).text
        except:
            return ""
