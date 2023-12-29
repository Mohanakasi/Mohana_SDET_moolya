import time

import selenium.common.exceptions

from practice_appium.selenium_methods.appium_sel_methods import appium_wrapper
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
class ixigo_flight_book(appium_wrapper):
    login_pop_up_close = (AppiumBy.ID, "com.ixigo:id/iv_cross_icon")
    from_city_btn = (AppiumBy.XPATH, "//android.view.View/..//android.widget.TextView[@text='From']")
    origin_city_text = (AppiumBy.XPATH, "//android.widget.TextView[@text='Origin city/airport code']/../../..//android.widget.EditText")
    cities_from = (AppiumBy.XPATH, "//android.widget.LinearLayout//android.widget.TextView")
    from_city_tap_xpath = (AppiumBy.XPATH, "//android.view.View//android.widget.TextView[@text='Vijayawada, India']")
    destination_city_text_field = (AppiumBy.XPATH, "//android.widget.TextView[@text='Destination city/airport code']/../../..//android.widget.EditText")
    cities_destination = (AppiumBy.XPATH, "//android.widget.TextView")
    destination_city_tap_xpath = (AppiumBy.XPATH, "//android.view.View//android.widget.TextView[@text='Bangalore, India']")
    date_pick_btn = (AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='com.ixigo:id/tv_form_field']//android.view.View)[1]")
    date = ['June', '2024', '30']
    desired_date = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{date[0]} {date[1]}']/..//android.widget.TextView[@text='{date[2]}']")
    def skipping_login(self):
        self.clicking_an_elmenet(self.login_pop_up_close)


    def click_on_from_city_button(self):
        self.clicking_an_elmenet(self.from_city_btn)


    def from_origin_city(self):
        self.city_tap_from_list(self.origin_city_text, 'vijaya', self.cities_from, 'vijayawada', self.from_city_tap_xpath)

    def destinationcity(self):
        self.city_tap_from_list(self.destination_city_text_field, 'bang', self.cities_destination, "kempegowda international airport", self.destination_city_tap_xpath)

    def date_pick(self):
        self.driver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()).scrollIntoView(text(\"EnterText\"))")
        self.tap_on_element(self.date_pick_btn)
        i = 1
        while i>0:
            month_fields = self.finding_elements((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.ixigo:id/title']"))
            for month in month_fields:
                if month.text == f'{self.date[0]} {self.date[1]}':
                    res = visibility_of_element_located(self.desired_date)
                    print(res.text)
                    if res:
                        desired_date = self.driver.find_element(*self.desired_date)
                        print(desired_date.text)
                        desired_date.click()
                        i -= 1
                        break
                    else:
                        self.driver.swipe(1030, 1161, 50, 353, duration=1300)

            else:
                self.driver.swipe(1030, 1161, 50, 353, duration=1300)
                time.sleep(3)


