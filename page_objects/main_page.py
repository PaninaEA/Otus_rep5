from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MainPage(BasePage):
    def search_box(self):
        self.get_element((By.CSS_SELECTOR, "#search"))

    def search_button(self):
        self.get_element((By.CSS_SELECTOR, "div#search button"))

    def cart_button(self):
        self.get_element((By.CSS_SELECTOR, "div#header-cart button[type='button']"))

    def menu_items(self):
        return self.get_elements((By.CSS_SELECTOR, "ul.nav.navbar-nav > li"))

    def dropdown_menu(self):
        return self.get_elements((By.CSS_SELECTOR, "li.nav-item.dropdown"))

    def dropdown_menu_for_players(self):
        self.click((By.CSS_SELECTOR, "li.nav-item.dropdown > a[href$='players']"))
        return self.get_elements((By.CSS_SELECTOR, "a[href*='players/']"))

    def get_product_on_main_page(self):
        return self.get_element((By.CSS_SELECTOR, "div.product-thumb h4 a"))

    def add_product_to_cart(self):
        product_name = self.get_product_on_main_page().text
        self.click((By.CSS_SELECTOR, "button[formaction$='cart.add']"))
        self.click((By.CSS_SELECTOR, "#alert button.btn-close"))
        self.click((By.XPATH, "//button[contains(text(),'item(s)')]"))
        self.get_element(
            (By.XPATH, f"//td[@class='text-start']/a[text()='{product_name}']")
        )

    def currency(self):
        return self.get_element((By.CSS_SELECTOR, "strong"))

    def product_price(self):
        return self.get_element((By.CSS_SELECTOR, "span.price-new"))

    def price_in_cart(self):
        return self.get_element((By.CSS_SELECTOR, "#header-cart button"))

    def change_currency(self, currency):
        self.currency().click()
        self.click((By.CSS_SELECTOR, f"li > a[href='{currency}']"))
