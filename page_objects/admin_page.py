import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminPage(BasePage):
    @allure.step("Открываю страницу администратора")
    def open_admin_page(self):
        self.logger.info(f"{self.class_name}: Open administration page")
        self.browser.get(self.browser.url + "/administration")

    @property
    @allure.step("Получаю заголовок страницы")
    def header(self):
        self.logger.info(f"{self.class_name}: Find header on page")
        return self.get_element((By.CSS_SELECTOR, "div.card-header"))

    @property
    @allure.step("Ищу форму авторизации")
    def form_login(self):
        self.logger.info(f"{self.class_name}: Find form for login on page")
        return self.get_element((By.CSS_SELECTOR, "div.card-body > form#form-login"))

    @property
    @allure.step("Получаю футер страницы")
    def footer(self):
        self.logger.info(f"{self.class_name}: Find footer on page")
        return self.get_element((By.CSS_SELECTOR, "footer#footer"))

    @property
    @allure.step("Проверяю название страницы")
    def title(self):
        self.logger.info(f"{self.class_name}: Find title of page")
        return self.browser.title

    @allure.step("Авторизуюсь на странице администратора")
    def login(self, login_pass):
        self.logger.info(f"{self.class_name}: Input admin credentials")
        self.input(
            (By.CSS_SELECTOR, "#input-username.form-control"), login_pass.split(":")[0]
        )
        self.input(
            (By.CSS_SELECTOR, "#input-password.form-control"), login_pass.split(":")[1]
        )
        self.logger.info(f"{self.class_name}: Click login")
        self.click((By.CSS_SELECTOR, "button[type='submit']"))
        self.logger.info(f"{self.class_name}: Authorization completed")
        self.get_element((By.CSS_SELECTOR, "#nav-profile"))

    @allure.step("Выхожу из аккаунта администратора")
    def logout(self):
        self.logger.info(f"{self.class_name}: Click logout")
        self.click((By.CSS_SELECTOR, "#nav-logout"))
        self.logger.info(f"{self.class_name}: Logout completed")
        self.get_element((By.CSS_SELECTOR, "#form-login"))

    @allure.step("Открываю каталог с продуктами")
    def open_products(self):
        self.logger.info(f"{self.class_name}: Open catalog of products")
        self.click((By.CSS_SELECTOR, "#menu-catalog"))
        self.click((By.XPATH, "//a[text()='Products']"))

    @allure.step("Добавляю новый продукт {product_data} в каталог")
    def add_new_product(self, product_data):
        self.logger.info(f"{self.class_name}: Add new product in catalog")
        self.click((By.CSS_SELECTOR, "div.float-end > a.btn.btn-primary"))
        self.logger.info(f"{self.class_name}: Input product data")
        self.input((By.CSS_SELECTOR, "#input-name-1"), product_data["product_name"])
        self.input(
            (By.CSS_SELECTOR, "#input-meta-title-1"), product_data["meta_tag_title"]
        )
        self.click((By.CSS_SELECTOR, "li.nav-item > a[href='#tab-data']"))
        self.input((By.CSS_SELECTOR, "#input-model"), product_data["model"])
        self.click((By.CSS_SELECTOR, "li.nav-item > a[href='#tab-seo']"))
        self.input((By.CSS_SELECTOR, "#input-keyword-0-1"), product_data["seo"])
        self.logger.info(f"{self.class_name}: Click add product button")
        self.click((By.CSS_SELECTOR, "div.float-end > button[type='submit']"))
        self.click((By.CSS_SELECTOR, "#alert button.btn-close"))
        self.click((By.CSS_SELECTOR, "div.float-end a.btn.btn-light"))

    @allure.step("Ищу продукт {product_name} в каталоге")
    def find_product(self, product_name):
        self.logger.info(f"{self.class_name}: Find product in catalog")
        self.input((By.CSS_SELECTOR, "#filter-product #input-name"), product_name)
        self.click((By.CSS_SELECTOR, "#filter-product #button-filter"))
        return self.check_element_exists(
            (By.CSS_SELECTOR, "#form-product tbody td.text-start")
        )

    @allure.step("Удаляю продукт из каталога")
    def delete_product(self):
        self.logger.info(f"{self.class_name}: Delete product from catalog")
        self.click((By.CSS_SELECTOR, "#form-product  input[type='checkbox']"))
        self.click((By.CSS_SELECTOR, "div.float-end button.btn.btn-danger"))
        self.logger.info(f"{self.class_name}: Click confirm delete")
        alert = self.get_alert()
        alert.accept()
