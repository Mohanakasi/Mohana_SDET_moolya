from pytest import fixture
from appium import webdriver
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
@fixture(scope='class')
def setup():
    cap: Dict[str, Any] = {
        "deviceName": "Mohana_VD",
        "platformName": "Android",
        "appPackage": "com.androidsample.generalstore",
        "appActivity": "com.androidsample.generalstore.SplashActivity"
    }
    driver = webdriver.Remote(r"http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(cap))
    driver.implicitly_wait(10)
    yield driver