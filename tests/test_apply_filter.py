import pytest
from assertpy import assert_that, soft_assertions

@pytest.mark.smoke
class TestFilter:

    def test_apply_filter(self,pom_instances,getLogger):

        #search product
        pom_instances['product_obj'].search_for_item("Tops")

        #get count before applying filter
        before_count = pom_instances['filter_obj'].count_by_applying_filter()

        #apply filter and get count
        pom_instances['filter_obj'].after_filter("men,men women")
        getLogger.info("Filter is applied based on gender")

        after_count = pom_instances['filter_obj'].count_after_applying_filter()
        getLogger.info(f"After applying filter {after_count}")

        with soft_assertions():
            assert_that(after_count).is_less_than(before_count)


    def test_product_match_the_selected_filters(self,pom_instances,getLogger):
        # search product
        pom_instances['product_obj'].search_for_item("kurta")

        # get count before applying filter
        before_count = pom_instances['filter_obj'].count_by_applying_filter()
        getLogger.info(f"before count {before_count}")

        # apply filter and get count
        pom_instances['filter_obj'].after_filter("women,men women")
        after_count = pom_instances['filter_obj'].count_after_applying_filter()
        getLogger.info(f"After applying filter {after_count}")
        pom_instances['filter_obj'].apply_filter_on_brands("Anouk")

        #get product details
        pom_instances['product_obj'].click_on_product()
        pom_instances['product_obj'].switch_to_product_window()
        url = pom_instances['home_obj'].get_url()

        with soft_assertions():
            assert_that(after_count).is_less_than(before_count)
            assert_that(url).contains("anouk","women")