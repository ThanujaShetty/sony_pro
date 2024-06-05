from selenium.webdriver.common.by import By

from src.Common.selenium_methods import selenium_wrapper


class FilterPage(selenium_wrapper):
    btn_gender_radio = (By.XPATH,'//input[@type="radio"]')
    btn_brand = (By.XPATH,'//input[@type="checkbox"]')
    filter_count = (By.CSS_SELECTOR,'span[class="title-count"]')
    after_filter = (By.CSS_SELECTOR,'span[class="title-count"]')

    def count_by_applying_filter(self):
        count = self.finding_element(self.filter_count).text
        a = ""
        for char in count:
            if char.isdigit():
                a += char
        prod_count = int(a)
        return prod_count

    def count_after_applying_filter(self):
        prod_count = self.finding_element(self.after_filter).text
        b = ""
        for product in prod_count:
            if product.isdigit():
                b += product
        after_fill = int(b)
        return after_fill

    def apply_filter_on_brands(self,brand_name):
        brands = self.find_multiple_ele(self.btn_brand)
        for brand in brands:
            b_name = brand.get_dom_attribute("value")
            if b_name == brand_name:
                brand.click()
                break
        return

    def apply_filter(self,category_name):
        category = self.find_multiple_ele(self.btn_gender_radio)
        for gender in category:
            g_name = gender.get_dom_attribute("value")
            if g_name == category_name:
                self.retry_element_click(gender)
                break
        return

