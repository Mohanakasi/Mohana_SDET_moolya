import time

from py_selenium_7_12.sel_methods.bank_sel_methods import Sel_re_use_functions
from selenium.webdriver.common.by import By
class bank_ops(Sel_re_use_functions):
    bank_mgr_btn = (By.XPATH, "//button[text()='Bank Manager Login']")
    add_customer_btn = (By.XPATH, "//button[contains(text(), 'Add Customer')]")
    first_name_field = (By.XPATH, "//input[@placeholder='First Name']")
    last_name_field = (By.XPATH, "//input[@placeholder='Last Name']")
    post_code_filed = (By.XPATH, "//input[@placeholder='Post Code']")
    add_cust_btn = (By.XPATH, "//button[text()='Add Customer']")
    open_ac = (By.XPATH, "//button[contains(text(), 'Open Account')]")
    def clicking_on_bank_mg_button(self):
        self.click_on_element(self.bank_mgr_btn)

    def click_on_add_csut_btn(self):
        self.click_on_element(self.add_customer_btn)

    def enter_first_name(self):
        self.entering_text(self.first_name_field, "Viswanath")

    def enter_last_name(self):
        self.entering_text(self.last_name_field, "Settipalli")


    def entering_post_code(self):
        self.entering_text(self.post_code_filed, 522003)


    def click_on_add_customer_btn(self):
        self.click_on_element(self.add_cust_btn)
        self.driver.switch_to.alert.accept()

    def click_on_open(self):
        self.click_on_element(self.open_ac)
        time.sleep(10)