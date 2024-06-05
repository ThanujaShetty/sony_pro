import pytest
from assertpy import soft_assertions, assert_that

from tests import home_page_title, men_page_title, women_page_title, Kids_page_title

@pytest.mark.usefixtures("setUp-tearDown")
class TestHome:

    def test_home_page_logo_validation(self,pom_instances,getLogger):
        pom_instances['product_obj'].search_for_item("Tops")
        pom_instances['product_obj'].click_on_product()
        pom_instances['product_obj'].switch_to_product_window()
        pom_instances['home_obj'].click_on_logo()
        hm_page_title = pom_instances['home_obj'].get_page_title()
        getLogger.info(f"Captured home page title {hm_page_title}")

        with soft_assertions():
            assert_that(hm_page_title).is_equal_to(home_page_title)

    def test_home_men_page_validation(self,pom_instances,getLogger):
        pom_instances['home_obj'].click_on_men_icon()
        pom_instances['product_obj'].search_for_item("shirts")
        actual_title = pom_instances['home_obj'].get_page_title()
        getLogger.info(f"Captured Men page title {actual_title}")

        with soft_assertions():
            assert_that(actual_title).is_equal_to(men_page_title)

    def test_home_women_page_validation(self, pom_instances, getLogger):
        pom_instances['home_obj'].click_on_women_icon()
        pom_instances['product_obj'].search_for_item("Tops")
        actual_title = pom_instances['home_obj'].get_page_title()
        getLogger.info(f"Captured Men page title {actual_title}")

        with soft_assertions():
            assert_that(actual_title).is_equal_to(women_page_title)


    def test_home_kids_page_validation(self, pom_instances, getLogger):
        pom_instances['home_obj'].click_on_kids_icon()
        pom_instances['product_obj'].search_for_item("Baby-dress")
        actual_title = pom_instances['home_obj'].get_page_title()
        getLogger.info(f"Captured Men page title {actual_title}")

        with soft_assertions():
            assert_that(actual_title).is_equal_to(Kids_page_title)






