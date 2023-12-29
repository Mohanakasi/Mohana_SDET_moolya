import time
from python_appium_data_driven.selenium_methods.appium_sel_methods import appium_wrapper
from appium.webdriver.common.appiumby import AppiumBy

class pom_true_caller(appium_wrapper):
    get_started_btn  = (AppiumBy.ID, "com.truecaller:id/nextButton")
    backup_skip = (AppiumBy.ID, "com.truecaller:id/button_skip")
    backup_skip_accept = (AppiumBy.ID, "android:id/button2")
    skip_subscription = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    skip_default_msg = (AppiumBy.ID, "com.truecaller:id/tooltipText")
    dialer_icon = (AppiumBy.ID, "com.truecaller:id/fab_icon")

    def clicking_on_get_started_btn(self):
        self.clicking_an_elmenet(self.get_started_btn)

    def clicking_on_backup_skip(self):
        self.clicking_an_elmenet(self.backup_skip)

    def accepting_skip(self):
        self.clicking_an_elmenet(self.backup_skip_accept)

    def close_subscription(self):
        self.clicking_an_elmenet(self.skip_subscription)

    def tap_on_default_msg(self):
        for _ in range(2):
            self.tap_on_element(self.skip_default_msg)


    def tap_on_dial_pad(self):
        self.tap_on_element(self.dialer_icon)
