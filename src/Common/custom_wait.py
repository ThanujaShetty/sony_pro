from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def wait_(func):
    def wrapper(*args,**kwargs):
        instance_ = args[0]
        loactor_ = args[1]
        wait = WebDriverWait(instance_.driver,timeout=10)
        wait.until(ec.presence_of_element_located(loactor_))
        return func(*args,**kwargs)
    return wrapper