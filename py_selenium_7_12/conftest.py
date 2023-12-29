import time

from selenium import webdriver
from pytest import fixture

@fixture(scope='class')
def setup_driver():
    print("no drivers")
    driver = webdriver.Edge()
    driver.get(r"https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    driver.maximize_window()
    time.sleep(5)
    yield driver
    driver.quit()

@fixture(scope='function')
def my_fixture2():
    print("executing 2nd fixture")
    print("end of the fixture")
    return "data from the 2nd fixture"