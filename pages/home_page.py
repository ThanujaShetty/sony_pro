from selenium.webdriver.common.by import By

from src.Common.selenium_methods import selenium_wrapper


class HomePage(selenium_wrapper):

    logo_icon = (By.CSS_SELECTOR,'div[class="desktop-logoContainer"]')
    search_box = (By.CSS_SELECTOR,'input[class="desktop-searchBar"]')
    lnk_women = (By.XPATH,'//div[@class="desktop-navLink"]//a[text()="Women"]')
    lnk_men = (By.XPATH,'//div[@class="desktop-navLink"]//a[text()="Men"]')
    lnk_kids = (By.XPATH,'//div[@class="desktop-navLink"]//a[text()="Kids"]')
    lnk_home_furniture = (By.XPATH,'//div[@class="desktop-navLink"]//a[text()="Home & Living"]')

    def click_on_logo(self):
        return self.driver.find_element(*self.logo_icon).click()

    def title_validation(self):
        return self.driver.title

    def click_on_women_icon(self):
        self.driver.find_element(*self.lnk_women).click()
        return

    def click_on_men_icon(self):
        self.driver.find_element(*self.lnk_men).click()
        return self.driver.current_url

    def click_on_kids_icon(self):
        self.driver.find_element(*self.lnk_kids).click()
        return

    def click_on_home_furniture(self):
        self.driver.click(*self.lnk_home_furniture)

    def get_page_title(self):
        return getattr(self.driver,'title')

    def get_url(self):
        return self.driver.current_url




    









