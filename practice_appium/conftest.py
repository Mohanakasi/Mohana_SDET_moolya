import time
from typing import Dict,Any
from pytest import fixture
from appium import webdriver
from appium.options.common import AppiumOptions
@fixture(scope="class")
def setup_driver():
    cap:Dict[str, Any]= {"deviceName":"Motorola moto g(60)",
                      "platformName":"Android",
                      "appPackage": "com.ixigo",
                      "appActivity": "com.ixigo.DefaultSplashScreenActivity"}

    driver  = webdriver.Remote(r"http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(cap))
    driver.implicitly_wait(20)
    yield driver