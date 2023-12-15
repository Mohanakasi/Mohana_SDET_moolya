from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
class visible_enable_check:
    def __call__(self, locator):
        self.locator = locator
        visible = visibility_of_element_located(locator)
        enabled = element_to_be_clickable(locator)
        return visible, enabled



def wait_synchro(func):
    def wait_wrapper(*args, **kwargs):
        instance_ = args[0]
        locator_ = args[1]
        custom_wait = WebDriverWait(instance_.driver, 50)
        wait_validator = visible_enable_check()(locator_)
        custom_wait.until(wait_validator[0])
        custom_wait.until(wait_validator[1])
        return func(*args, **kwargs)
    return wait_wrapper


class Sel_re_use_functions:

    def __init__(self, driver):
        self.driver = driver

    @wait_synchro
    def finding_an_elmenet(self, locator):
        return self.driver.find_element(*locator)

    @wait_synchro
    def finding_elements(self, locator):
        return self.driver.find_elements(*locator)


    @wait_synchro
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @wait_synchro
    def entering_text(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)



    def mouse_hover_to_element(self, locator):
        mouse_action = ActionChains(self.driver)
        element = self.finding_an_elmenet(locator)
        mouse_action.move_to_element(element)


    def scroll_to_element(self, locator):
        element = self.finding_an_elmenet(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def switch_to_new_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])


    def selecting_item_drop_down(self, list_box):
        drop_down = Select(list_box)