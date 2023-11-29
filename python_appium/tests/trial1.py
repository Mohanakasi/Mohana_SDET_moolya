# import time
import pytest
# from appium import webdriver
# from typing import Any, Dict
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
from python_appium.pages.add_to_cart import pom_general_store
# from pytest import fixture
# cap: Dict[str, Any] = {
#     "deviceName" : "Mohana_VD",
#     "platformName": "Android",
#     "appPackage": "com.androidsample.generalstore",
#     "appActivity": "com.androidsample.generalstore.SplashActivity"
# }
# driver = webdriver.Remote(r"http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(cap))
# driver.implicitly_wait(10)
# driver.find_element(AppiumBy.ID, "android:id/text1").click()
# time.sleep(3)
#
# i = 1
# while i > 0:
#     list_ = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView")
#     for country in list_:
#         if country.text == 'Bhutan':
#             country.click()
#             i -= 1
#             break
#     else:
#         driver.swipe(789, 2088, 178, 595, 500)
#         time.sleep(4)
# driver.find_element(AppiumBy.ID, "com.androidsample.generalstore:id/nameField").send_keys("Mohana kasi")
# driver.find_element(AppiumBy.ID, "com.androidsample.generalstore:id/radioMale").click()
# driver.find_element(AppiumBy.ID, "com.androidsample.generalstore:id/btnLetsShop").click()
# time.sleep(5)
# i = 1
# while i > 0:
#     list_= driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView")
#     for shoe in list_:
#         if shoe.text == "Converse All Star":
#             driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Converse All Star']/..//android.widget.TextView[@text='ADD TO CART']").click()
#             i -=1
#             break
#     else:
#         driver.swipe(1052, 1063, 28, 256, 500)
#         time.sleep(4)
# driver.find_element(AppiumBy.ID, "com.androidsample.generalstore:id/appbar_btn_cart").click()
# time.sleep(4)
# driver.find_element(AppiumBy.XPATH, "//android.widget.CheckBox[@text='Send me e-mails on discounts related to selected products in future']").click()
# driver.find_element(AppiumBy.ID, "com.androidsample.generalstore:id/btnProceed").click()