import time

from assertpy import soft_assertions, assert_that
from src.Common import config

from tests import error_message, product_home_page_title, detail_product_obj_title


class TestProductSearch:

    def test_search_product(self,pom_instances,getLogger):
        pom_instances['product_obj'].search_for_item("kurta")
        home_title = pom_instances['product_obj'].get_product_homepage_title()

        with soft_assertions():
            assert_that(home_title).is_equal_to(product_home_page_title)


    def test_invalid_search(self,pom_instances,getLogger):
        pom_instances['product_obj'].search_for_item("hgjhsgjshbgh%$#")
        msg = pom_instances['product_obj'].get_error_message()

        with soft_assertions():
            assert_that(msg).is_equal_to(error_message)

    def test_product_navigation(self,pom_instances,getLogger):
        pom_instances['product_obj'].search_for_item("Kurta")
        pom_instances['product_obj'].get_product_homepage_title()
        pom_instances['product_obj'].click_on_product()
        pom_instances['product_obj'].switch_to_product_window()

        product_title = pom_instances['product_obj'].get_product_page_title()
        getLogger.info(f"product page title {product_title}")

        with soft_assertions():
            assert_that(product_title).is_equal_to(detail_product_obj_title)

    def test_product_details(self,pom_instances,getLogger):
        pom_instances['product_obj'].search_for_item("Tops")
        pom_instances['product_obj'].get_product_homepage_title()
        pom_instances['product_obj'].click_on_product()
        pom_instances['product_obj'].switch_to_product_window()

        #get product details
        pp_name = pom_instances['product_obj'].item_name
        getLogger.info(f"product title {pp_name}")

        product_price = pom_instances['product_obj'].product_price
        getLogger.info(f"product price {product_price}")

        symbol = pom_instances['product_obj'].check_currency_inr()

        pom_instances['shopping_obj'].select_size(config.size)
        pom_instances['shopping_obj'].click_on_add_to_cart()
        pom_instances['shopping_obj'].click_on_Bag()

        name = pom_instances['shopping_obj'].product_name_in_cart()

        with soft_assertions():
            assert_that(pp_name).is_equal_to(name)
            assert_that(symbol).is_equal_to(config.symbol)








