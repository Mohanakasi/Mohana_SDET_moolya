# import time
import pytest
# from appium import webdriver
# from typing import Any, Dict
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
from python_appium.pages.add_to_cart import pom_general_store
# from pytest import fixture
@pytest.mark.usefixtures("setup")
class Test_gen_store_cart:

    def test_adding_shoes_to_cart(self, setup):
        gen_st_obj = pom_general_store(setup)
        gen_st_obj.selecting_country()
        gen_st_obj.entering_name()
        gen_st_obj.selecting_gender_option()
        gen_st_obj.proceeding_to_shoping()
        gen_st_obj.selecting_shoe_from_items()
        gen_st_obj.proceeding_to_check_out()
        gen_st_obj.email_subsription()
        gen_st_obj.proceed_to_payment()

