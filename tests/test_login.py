import time

from pages.login_page import LoginPage
from src.Common import config
from src.Common.base import BaseTest


class TestLogin:

    def test_valid_login(self,pom_instances):
        pom_instances['login_obj'].click_on_login()
        pom_instances['login_obj'].enter_mobile_no(config.mobile_no)
        pom_instances['login_obj'].click_on_password_link()