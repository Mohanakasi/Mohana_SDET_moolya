import time
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from python_appium_data_driven.Data_setup.excel_read import locators_fetch_from_excel
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
        wait_ = WebDriverWait(instance_.driver, 50)
        v = El_vis_enab_check()(locat_)
        wait_.until(v[0])
        wait_.until(v[1])
        return func(*args, **kwargs)
    return wrapper


class appium_wrapper:
    def __init__(self, driver, excel_sheet_path, sheet_name, column1, coloumn2):
        self.driver = driver
        locators_fetch_from_excel(excel_sheet_path, sheet_name, column1, coloumn2)

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
