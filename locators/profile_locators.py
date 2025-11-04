from selenium.webdriver.common.by import By


class ProfileLocators:
    MY_ADS_SECTION = (By.CSS_SELECTOR, "[data-testid='my-ads']")
    AD_ITEM = (By.CSS_SELECTOR, "[data-testid='ad-item']")
    AD_TITLE = (By.CSS_SELECTOR, "[data-testid='ad-title']")
