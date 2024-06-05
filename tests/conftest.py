import configparser
import inspect
import logging
import time

import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from pages.cart_page import CartPage
from pages.filter_page import FilterPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from src.Common import config
from src.Common.selenium_methods import selenium_wrapper


# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default=config.browser)

# @pytest.fixture
# def getBrowser(request):
#     _browser = request.config.getoption("--browser")
#     return _browser

@pytest.fixture(scope='class')
def getLogger():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)
    return logger

@pytest.fixture(scope='function')
def pom_instances(request,setUp_tearDown):
    instances = {
        'home_obj' :HomePage(setUp_tearDown),
        'base_obj' : selenium_wrapper(setUp_tearDown),
        'product_obj' : ProductPage(setUp_tearDown),
        'filter_obj' : FilterPage(setUp_tearDown),
        'login_obj': LoginPage(setUp_tearDown),
        'shopping_obj' : CartPage(setUp_tearDown)

    }
    return instances


@pytest.fixture(scope='function')
def setUp_tearDown(request,getLogger):
    config = configparser.ConfigParser()
    config.read('config.ini',encoding='utf-8')

    try:
        browser_name = config.get('Browser','browser_name')
    except configparser.NoSectionError as e:
        getLogger.error(f"Error occured : {e}")

    implicit_wait_time = config.getint('Browser','implicitly_wait_time')
    url = config.get('ApplicationSettings','app_url')
    if browser_name == "Chrome":

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        ch_ = Options()
        ch_.add_experimental_option("detach",True)
    elif browser_name == "Edge":
        driver = webdriver.Edge()
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else :
        raise ValueError(f"Unsupported browser :{browser_name}")
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(implicit_wait_time)
    request.cls.driver = driver
    yield request.cls.driver
    request.cls.driver.quit()






