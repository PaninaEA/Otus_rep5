import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class UserPage(BasePage):
    @allure.step("Открываю страницу регистрации нового пользователя")
    def open_register_user_page(self):
        self.logger.info(f"{self.class_name}: Open page for register user")
        self.click((By.XPATH, "//span[text()='My Account']"))
        self.click((By.XPATH, "//a[text()='Register']"))

    @allure.step("Проверяю обязательные для заполнения поля")
    def required_fields(self):
        self.logger.info(f"{self.class_name}: Find required fields")
        return self.get_elements(
            (By.CSS_SELECTOR, "#form-register > fieldset > div.row.mb-3.required")
        )

    @allure.step("Проверяю пункты в меню пользователя")
    def user_menu_items(self):
        self.logger.info(f"{self.class_name}: Find items in user menu")
        return self.get_elements((By.CSS_SELECTOR, "div > a.list-group-item"))

    @allure.step("Добавляю нового пользователя")
    def register_new_user(self, user_data):
        self.logger.info(f"{self.class_name}: Input user data")
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
        self.logger.info(f"{self.class_name}: Click button for register")
        self.click((By.CSS_SELECTOR, "div.text-end > button[type='submit']"))
        self.get_element((By.CSS_SELECTOR, "#common-success"))
