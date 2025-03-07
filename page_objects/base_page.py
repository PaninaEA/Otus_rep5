from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def get_element(self, locator: tuple, timeout=2):
        self.logger.debug("%s: Find element: %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_elements(self, locator: tuple, timeout=2):
        self.logger.debug("%s: Find elements: %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def get_alert(self, timeout=2):
        self.logger.debug(f"{self.class_name}: Alert is_present")
        return WebDriverWait(self.browser, timeout).until(EC.alert_is_present())

    def click(self, locator: tuple):
        self.logger.debug("%s: Click element: %s" % (self.class_name, str(locator)))
        ActionChains(self.browser).move_to_element(
            self.get_element(locator)
        ).click().perform()

    def input(self, locator: tuple, data: str):
        self.logger.debug(
            "%s: Input data to element: %s" % (self.class_name, str(locator))
        )
        self.get_element(locator).click()
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(data)

    def check_element_exists(self, locator: tuple):
        self.logger.info(
            "%s: Check for element exists: %s" % (self.class_name, str(locator))
        )
        try:
            return self.get_element(locator)
        except TimeoutException:
            return False
