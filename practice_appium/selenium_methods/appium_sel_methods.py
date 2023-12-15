import time
from datetime import datetime

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
class El_vis_enab_check():
    def __call__(self, locator_):
        self.locator_ = locator_
        displayed = visibility_of_element_located(locator_)
        enabled = element_to_be_clickable(locator_)
        return displayed,enabled

def wait_deco(func):
    def wrapper(*args, **kwargs):
        instance_ = args[0]
        locat_ =    args[1]
        wait_ = WebDriverWait(instance_.driver, 30)
        v = El_vis_enab_check()(locat_)
        wait_.until(v[0])
        wait_.until(v[1])
        return func(*args, **kwargs)
    return wrapper


class appium_wrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait_deco
    def finding_an_element(self, locator):
        return self.driver.find_element(*locator)

    @wait_deco
    def finding_elements(self, locator):
        return self.driver.find_elements(*locator)

    @wait_deco
    def clicking_an_elmenet(self, locator):
        self.driver.find_element(*locator).click()

    @wait_deco
    def entering_text_into_text_field(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)


    def page_screen_shot_capture(self, path,s_shot_name):
        time.sleep(4)
        t_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        file_name = s_shot_name+t_stamp+'.png'
        self.driver.get_screenshot_as_file(path+file_name)

    def city_tap_from_list(self, text_filed, data_to_enter, all_cities_xpath, matching_city_name, city_tap_xpath):
        self.entering_text_into_text_field(text_filed, data_to_enter)
        i = 1
        while i > 0:
            origin_city_items = self.finding_elements(all_cities_xpath)
            for city_name in origin_city_items:
                if city_name.text.lower() == matching_city_name:
                    actions = TouchAction(self.driver)
                    desired_city = self.finding_an_element(city_tap_xpath)
                    actions.tap(desired_city).perform()
                    i -= 1
                    break
            else:
                self.driver.swipe(1080, 895, 0, 675)
                time.sleep(4)


    def tap_on_element(self, element_xpah):
        actions = TouchAction(self.driver)
        element = self.finding_an_element(element_xpah)
        actions.tap(element).perform()