from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdminPage(BasePage):
    def open_admin_page(self):
        self.browser.get(self.browser.url + "/administration")

    def header(self):
        self.get_element((By.CSS_SELECTOR, "div.card-header"))

    def form_login(self):
        self.get_element((By.CSS_SELECTOR, "div.card-body > form#form-login"))

    def footer(self):
        self.get_element((By.CSS_SELECTOR, "footer#footer"))

    def title(self):
        return self.browser.title

    def login(self, login_pass):
        self.input(
            (By.CSS_SELECTOR, "#input-username.form-control"), login_pass.split(":")[0]
        )
        self.input(
            (By.CSS_SELECTOR, "#input-password.form-control"), login_pass.split(":")[1]
        )
        self.click((By.CSS_SELECTOR, "button[type='submit']"))
        self.get_element((By.CSS_SELECTOR, "#nav-profile"))

    def logout(self):
        self.click((By.CSS_SELECTOR, "#nav-logout"))
        self.get_element((By.CSS_SELECTOR, "#form-login"))

    def open_products(self):
        self.click((By.CSS_SELECTOR, "#menu-catalog"))
        self.click((By.XPATH, "//a[text()='Products']"))

    def add_new_product(self, product_data):
        self.click((By.CSS_SELECTOR, "div.float-end > a.btn.btn-primary"))
        self.input((By.CSS_SELECTOR, "#input-name-1"), product_data["product_name"])
        self.input(
            (By.CSS_SELECTOR, "#input-meta-title-1"), product_data["meta_tag_title"]
        )
        self.click((By.CSS_SELECTOR, "li.nav-item > a[href='#tab-data']"))
        self.input((By.CSS_SELECTOR, "#input-model"), product_data["model"])
        self.click((By.CSS_SELECTOR, "li.nav-item > a[href='#tab-seo']"))
        self.input((By.CSS_SELECTOR, "#input-keyword-0-1"), product_data["seo"])
        self.click((By.CSS_SELECTOR, "div.float-end > button[type='submit']"))
        self.click((By.CSS_SELECTOR, "#alert button.btn-close"))
        self.click((By.CSS_SELECTOR, "div.float-end a.btn.btn-light"))

    def find_product(self, product_name):
        self.input((By.CSS_SELECTOR, "#filter-product #input-name"), product_name)
        self.click((By.CSS_SELECTOR, "#filter-product #button-filter"))
        return self.check_element_exists(
            (By.CSS_SELECTOR, "#form-product tbody td.text-start")
        )

    def delete_product(self):
        self.click((By.CSS_SELECTOR, "#form-product  input[type='checkbox']"))
        self.click((By.CSS_SELECTOR, "div.float-end button.btn.btn-danger"))
        alert = self.get_alert()
        alert.accept()
