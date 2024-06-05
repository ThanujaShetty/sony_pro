from selenium.webdriver.common.by import By
from src.Common.selenium_methods import selenium_wrapper


class LoginPage(selenium_wrapper):



    profile_icon = (By.XPATH,'//span[text()="Profile"]')
    txt_mobile = (By.CSS_SELECTOR,'input[type="tel"]')
    btn_continue = (By.CSS_SELECTOR,'div[class="submitBottomOption"]')
    btn_login = (By.XPATH,'//a[text()="login / Signup"]')
    err_mesg = (By.CSS_SELECTOR, "h3[data-test='error']")
    lnk_password = (By.XPATH,'//span[text()=" Password "]')

    def click_on_login(self):
        self.mouse_hover(self.profile_icon)
        self.finding_element(self.btn_login).click()
        return

    def enter_mobile_no(self,mobile_no):
        self.finding_element(self.txt_mobile).click()
        self.driver.send_keys(self.txt_mobile,mobile_no)
        self.driver.click(self.btn_continue)
        return

    def click_on_password_link(self):
        self.finding_element(self.btn_continue).click()
        self.finding_element(self.lnk_password).click()
        return