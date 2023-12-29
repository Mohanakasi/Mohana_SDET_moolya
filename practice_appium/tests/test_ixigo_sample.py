from practice_appium.pages.intro_page import ixigo_flight_book
from pytest import mark
@mark.usefixtures("setup_driver")
class Test_ixigo_demo:

    def test_case1(self, setup_driver):
        obj1 = ixigo_flight_book(setup_driver)
        obj1.skipping_login()
        # obj1.click_on_from_city_button()
        # obj1.from_origin_city()
        # obj1.destinationcity()
        obj1.date_pick()
