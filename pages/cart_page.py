import re
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from src.Common.selenium_methods import selenium_wrapper


class CartPage(selenium_wrapper):
    btn_add_to_cart = (By.XPATH,'//div[text()="ADD TO BAG"]')
    size_extra_small = (By.XPATH,'//p[text()="XS"]')
    size_small = (By.XPATH,'//p[text()="S"]')
    size_medium = (By.XPATH, '//p[text()="M"]')
    size_large = (By.XPATH, '//p[text()="L"]')
    size_extra_large = (By.XPATH, '//p[text()="XL"]')
    size_extra_larger = (By.XPATH, '//p[text()="XXL"]')
    cart_btn = (By.XPATH,'//span[text()="Bag"]')
    product_name = (By.CSS_SELECTOR,'div[class="itemContainer-base-brand"]')
    product_quantity = (By.XPATH,'//span[contains(@class,"desktop-badge")]')
    product_price = (By.CSS_SELECTOR,'div[class="itemComponents-base-price itemComponents-base-bold "]')
    size_details =(By.CSS_SELECTOR,'.itemComponents-base-size')



    def click_on_add_to_cart(self):
        ele = self.finding_element(self.btn_add_to_cart)
        ele.click()

    def select_size(self,size):
        try:
            if size == "S":
                ele = self.finding_element(self.size_small)
                ele.click()
            elif size == "XS":
                ele = self.finding_element(self.size_extra_small)
                ele.click()
            elif size == "M":
                ele = self.finding_element(self.size_medium)
                ele.click()
            elif size == "L":
                ele = self.finding_element(self.size_large)
                ele.click()
            elif size == "XL":
                ele = self.finding_element(self.size_extra_large)
                ele.click()
            elif size == "XXL":
                ele = self.finding_element(self.size_extra_larger)
                ele.click()
        except NoSuchElementException:
            time.sleep(2)

    def click_on_Bag(self):
        return self.finding_element(self.cart_btn).click()

    def product_name_in_cart(self):
        return self.finding_element(self.product_name).text

    def cart_quantity(self):
        return self.get_count(self.product_quantity)

    def product_price_in_cart(self):
        return self.finding_element(self.product_price).text

    def item_quantity_check(self,total_quantity):
        temp_quantity = self.finding_element(self.product_quantity).text
        quantity_fetch = int(''.join(re.findall(r"\d",temp_quantity)))
        return quantity_fetch

    def go_back(self):
        self.driver.refresh()

    def get_size_in_cart(self):
        ele = self.finding_element(self.size_details).text
        return ele

