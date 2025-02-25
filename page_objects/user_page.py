from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class UserPage(BasePage):
    def open_register_user_page(self):
        self.click((By.XPATH, "//span[text()='My Account']"))
        self.click((By.XPATH, "//a[text()='Register']"))

    def required_fields(self):
        return self.get_elements(
            (By.CSS_SELECTOR, "#form-register > fieldset > div.row.mb-3.required")
        )

    def user_menu_items(self):
        return self.get_elements((By.CSS_SELECTOR, "div > a.list-group-item"))

    def register_new_user(self, user_data):
        self.input(
            (By.CSS_SELECTOR, "input#input-firstname.form-control"),
            user_data["firstname"],
        )
        self.input(
            (By.CSS_SELECTOR, "input#input-lastname.form-control"),
            user_data["lastname"],
        )
        self.input(
            (By.CSS_SELECTOR, "input#input-email.form-control"), user_data["email"]
        )
        self.input(
            (By.CSS_SELECTOR, "input#input-password.form-control"),
            user_data["password"],
        )
        self.click((By.NAME, "agree"))
        self.click((By.CSS_SELECTOR, "div.text-end > button[type='submit']"))
        self.get_element((By.CSS_SELECTOR, "#common-success"))
