

from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from src.Common.custom_wait import wait_



class selenium_wrapper():

    def __init__(self, driver):
        self.driver = driver

    @wait_
    def enter_text(self,by_locator,value):
        return self.driver.find_element(*by_locator).send_keys(value)

    @wait_
    def do_click(self, by_locator):
        return self.driver.click(*by_locator)

    @wait_
    def get_text(self, by_locator):
      return self.driver.find_element(by_locator).get_attribute("innerText")

    @wait_
    def get_count(self, by_locator):
        return len(by_locator)

    @wait_
    def get_element(self, by_locator):
        return self.driver.find_elements(by_locator)


    def select_text(self, by_locator, option):
        select = Select(self.get_element(by_locator))
        select.select_by_visible_text(option)
        return

    def finding_element(self,by_locator):
        return self.driver.find_element(*by_locator)

    def mouse_hover(self, element):
        locator_type, locator_value = element
        action = ActionChains(self.driver)
        element = self.driver.find_element(locator_type, locator_value)
        action.move_to_element(element).perform()

    @wait_
    def page_down(self,count):
        for i in range(0,count):
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        return

    def accept_alert(self):
        alert =Alert(self.driver)
        self.driver.switch_to_alert()
        alert.accept()
        return

    @wait_
    def dismiss_alert(self):
        alert =Alert(self.driver)
        self.driver.switch_to_alert()
        alert.dismiss()
        return

    @wait_
    def find_multiple_ele(self,by_locator):
        return self.driver.find_elements(*by_locator)

    @wait_
    def retry_element_click(self,element,max_reties = 3):
        for _ in range(max_reties):
            try:
                self.driver.execute_script("arguments[0].click();",element)
                WebDriverWait(self.driver,10).until(ec.element_to_be_selected(element))
                return
            except StaleElementReferenceException :
                pass
        return

