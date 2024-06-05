from assertpy import soft_assertions, assert_that

from src.Common import config
from src.Common.config import quantity


class TestShopping:

    def test_add_product_to_cart(self,pom_instances,getLogger):

        pom_instances['product_obj'].search_input("Tops")
        pom_instances['product_obj'].click_on_product()
        pom_instances['product_obj'].switch_to_product_window()

        pom_instances['shopping_obj'].select_size(config.size)
        pom_instances['shopping_obj'].click_on_add_to_cart()
        pom_instances['shopping_obj'].click_on_Bag()

        pom_instances['shopping_obj'].product_name_in_cart()
        prod_size = pom_instances['shopping_obj'].get_size_in_cart()

        with soft_assertions():
            assert_that(prod_size).contains(config.size)

    def test_validating_product_in_cart(self,pom_instances,getLogger):
        pom_instances['product_obj'].search_input("Tops")
        pom_instances['product_obj'].click_on_product()
        pom_instances['product_obj'].switch_to_product_window()

        pom_instances['shopping_obj'].select_size(config.size)
        pom_instances['shopping_obj'].click_on_add_to_cart()

        pom_instances['shopping_obj'].go_back()
        pom_instances['shopping_obj'].select_size(config.size)
        pom_instances['shopping_obj'].click_on_add_to_cart()

        cart_quantity = pom_instances['shopping_obj'].cart_quantity()

        with soft_assertions():
            assert_that(cart_quantity).is_equal_to(quantity)
