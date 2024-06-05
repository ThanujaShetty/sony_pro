import re
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.Common import config
from src.Common.selenium_methods import selenium_wrapper


class ProductPage(selenium_wrapper):


    search_box = (By.CSS_SELECTOR,'input[class="desktop-searchBar"]')
    invalid_search = ((By.CSS_SELECTOR,'input[class="desktop-searchBar"]'), config.invalid_items)
    product_name = (By.XPATH,'//ul[@class="results-base"]//li[2]')
    invalid_error_msg = (By.XPATH,'//p[contains(text(),"find any matches! ")]')
    product_title_locator =(By.CSS_SELECTOR,'.pdp-title')
    product_price_locator = (By.CSS_SELECTOR,'.pdp-price')
    currency_symbol = (By.CSS_SELECTOR,'span[class="pdp-price"]')

    @property
    def search_input(self):
        return self.driver.find_element(*self.search_box)

    def search_for_item(self,item_name):
        self.search_input.clear()
        self.search_input.send_keys(item_name)
        self.search_input.send_keys(Keys.ENTER)

    def get_product_page_title(self):
        return self.driver.title

    def get_product_homepage_title(self):
        return self.driver.title

    def get_main_page_window(self):
        main_window_handles = self.driver.window_handles[0]
        return main_window_handles

    def switch_to_product_window(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != self.get_main_page_window():
                self.driver.switch_to.window(handle)
                title = self.driver.title
                break
        return

    def click_on_product(self):
        ele = self.driver.find_elements(*self.product_name)
        ele[0].click()

    def invalid_product_search(self):
        element = self.finding_element(self.invalid_search[0])
        self.enter_text(self.invalid_search[0], self.invalid_search[1])
        element.send_keys(Keys.ENTER)
        return self.get_error_message()

    @property
    def item_name(self):
        return self.driver.find_element(*self.product_title_locator).text

    def get_error_message(self):
        error_message = self.driver.find_element(*self.invalid_error_msg).text
        return error_message

    @property
    def product_price(self):
        price = self.driver.find_element(*self.product_price_locator).text
        return price

    def check_currency_inr(self):
        price = self.driver.find_element(*self.currency_symbol).text
        item_price_symbol = re.findall(r'[^a-zA-Z0-9\s]',price)
        price_in_INR = "".join(item_price_symbol)
        return price_in_INR








