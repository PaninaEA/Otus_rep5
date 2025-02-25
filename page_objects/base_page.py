from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def get_element(self, locator: tuple, timeout=2):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_elements(self, locator: tuple, timeout=2):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def get_alert(self, timeout=2):
        return WebDriverWait(self.browser, timeout).until(EC.alert_is_present())

    def click(self, locator: tuple):
        ActionChains(self.browser).move_to_element(
            self.get_element(locator)
        ).click().perform()

    def input(self, locator: tuple, data: str):
        self.get_element(locator).click()
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(data)

    def check_element_exists(self, locator: tuple):
        try:
            self.get_element(locator)
        except TimeoutException:
            return False
        return self.get_element(locator)
