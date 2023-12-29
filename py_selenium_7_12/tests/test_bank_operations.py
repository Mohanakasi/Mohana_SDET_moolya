from py_selenium_7_12.pages.bank_manager import bank_ops
from pytest import mark
@mark.usefixtures("my_fixture2", "setup_driver")
class Test_bank_manager:

    def test_adding_a_customer(self, setup_driver, my_fixture2):
        add_obj = bank_ops(setup_driver)
        print(my_fixture2, "fixture2 came")
        add_obj.clicking_on_bank_mg_button()
        add_obj.click_on_add_csut_btn()
        add_obj.enter_first_name()
        add_obj.enter_last_name()
        add_obj.entering_post_code()
        add_obj.click_on_add_customer_btn()
        add_obj.click_on_open()

