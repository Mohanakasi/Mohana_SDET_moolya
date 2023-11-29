import time
from python_appium_data_driven.selenium_methods.appium_sel_methods import appium_wrapper
from appium.webdriver.common.appiumby import AppiumBy
from python_appium_data_driven.Data_setup.excel_read import Excel_test_data
class pom_general_store(appium_wrapper, Excel_test_data):
    # country_drop_down = (AppiumBy.ID, "android:id/text1")
    # country_items = (AppiumBy.XPATH, "//android.widget.TextView")
    # name_field = ((AppiumBy.ID, "com.androidsample.generalstore:id/nameField"), "Mohana kasi")
    # gender_radio_male = (AppiumBy.ID, "com.androidsample.generalstore:id/radioMale")
    # proceed_btn = (AppiumBy.ID, "com.androidsample.generalstore:id/btnLetsShop")
    # shoe_items = (AppiumBy.XPATH, "//android.widget.TextView")
    # add_to_cart_btn_shoe = (AppiumBy.XPATH, "//android.widget.TextView[@text='Converse All Star']/..//android.widget.TextView[@text='ADD TO CART']")
    # cart_button = (AppiumBy.ID, "com.androidsample.generalstore:id/appbar_btn_cart")
    # email_sub_check_box = (AppiumBy.XPATH, "//android.widget.CheckBox[@text='Send me e-mails on discounts related to selected products in future']")
    # payment_proceed_btn = (AppiumBy.ID, "com.androidsample.generalstore:id/btnProceed")
    def selecting_country(self):
        self.finding_an_element(self.country_drop_down).click()
        time.sleep(3)
        i = 1
        while i > 0:
            list_ = self.finding_elements(self.country_items)
            for country in list_:
                if country.text == 'Bhutan':
                    country.click()
                    i -= 1
                    break
            else:
                self.driver.swipe(789, 2088, 178, 595, 500)
                time.sleep(4)

    def entering_name(self):
        self.entering_text_into_text_field(*self.name_field)

    def selecting_gender_option(self):
        self.clicking_an_elmenet(self.gender_radio_male)

    def proceeding_to_shoping(self):
        self.clicking_an_elmenet(self.proceed_btn)

    def selecting_shoe_from_items(self):
        time.sleep(5)
        i = 1
        while i > 0:
            list_ = self.finding_elements(self.shoe_items)
            for shoe in list_:
                if shoe.text == "Converse All Star":
                    self.finding_an_element(self.add_to_cart_btn_shoe).click()
                    i -= 1
                    break
            else:
                self.driver.swipe(1052, 1063, 28, 256, 500)
                time.sleep(4)

    def proceeding_to_check_out(self):
        self.clicking_an_elmenet(self.cart_button)

    def email_subsription(self):
        self.clicking_an_elmenet(self.email_sub_check_box)

    def proceed_to_payment(self):
        self.clicking_an_elmenet(self.payment_proceed_btn)

