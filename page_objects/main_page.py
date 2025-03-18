import allure
from currency_symbols import CurrencySymbols
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MainPage(BasePage):
    @property
    @allure.step("Ищу поле поиска на странице")
    def search_box(self):
        self.logger.info(f"{self.class_name}: Find search box")
        return self.get_element((By.CSS_SELECTOR, "#search"))

    @property
    @allure.step("Ищу кнопку поиска на странице")
    def search_button(self):
        self.logger.info(f"{self.class_name}: Find search button")
        return self.get_element((By.CSS_SELECTOR, "div#search button"))

    @property
    @allure.step("Ищу кнопку перехода в корзину")
    def cart_button(self):
        self.logger.info(f"{self.class_name}: Find cart button")
        return self.get_element(
            (By.CSS_SELECTOR, "div#header-cart button[type='button']")
        )

    @allure.step("Проверяю пункты главного меню")
    def menu_items(self):
        self.logger.info(f"{self.class_name}: Find items in main menu")
        return self.get_elements((By.CSS_SELECTOR, "ul.nav.navbar-nav > li"))

    @allure.step("Проверяю выпадающие списки в пунктах главного меню")
    def dropdown_menu(self):
        self.logger.info(f"{self.class_name}: Find dropdown menu")
        return self.get_elements((By.CSS_SELECTOR, "li.nav-item.dropdown"))

    @allure.step("Проверяю выпадающий список для пункта меню MP3 Players")
    def dropdown_menu_for_players(self):
        self.logger.info(f"{self.class_name}: Find dropdown menu for players")
        self.click((By.CSS_SELECTOR, "li.nav-item.dropdown > a[href$='players']"))
        return self.get_elements((By.CSS_SELECTOR, "a[href*='players/']"))

    @allure.step("Ищу продукт на главной странице")
    def get_some_product_on_main_page(self):
        self.logger.info(f"{self.class_name}: Find some product on main page")
        return self.get_element((By.CSS_SELECTOR, "div.product-thumb h4 a"))

    @allure.step("Нажимаю на продукт на главной странице")
    def click_product_on_main_page(self):
        self.logger.info(f"{self.class_name}: Click product on main page")
        product_active = self.get_element((By.CSS_SELECTOR, "div.carousel-item.active"))
        product_active.click()

    @allure.step("Добавляю продукт c главной страницы в корзину")
    def add_product_to_cart(self):
        product_name = self.get_some_product_on_main_page().text
        self.logger.info(f"{self.class_name}: Add product {product_name} to cart")
        self.scroll_to_element((By.CSS_SELECTOR, "div.button-group"))
        self.click((By.CSS_SELECTOR, "button[formaction$='cart.add']"))
        self.click((By.CSS_SELECTOR, "#alert button.btn-close"))
        return product_name

    @allure.step("Проверяю продукт в корзине")
    def get_product_in_cart(self):
        self.logger.info(f"{self.class_name}: Check product in cart")
        self.scroll_to_element((By.CSS_SELECTOR, "header"))
        self.click((By.XPATH, "//button[contains(text(),'item(s)')]"))
        return self.get_element((By.CSS_SELECTOR, "td.text-start > a")).text

    @property
    @allure.step("Получаю валюту на главной странице")
    def currency(self):
        self.logger.info(f"{self.class_name}: Find currency in main menu")
        return self.get_element((By.CSS_SELECTOR, "strong"))

    @property
    @allure.step("Получаю цену продукта на главной странице")
    def product_price(self):
        self.logger.info(f"{self.class_name}: Find price of product on main page")
        return self.get_element((By.CSS_SELECTOR, "span.price-new"))

    @property
    @allure.step("Получаю цену в корзине на главной странице")
    def price_in_cart(self):
        self.logger.info(
            f"{self.class_name}: Find price of product in cart on main page"
        )
        return self.get_element((By.CSS_SELECTOR, "#header-cart button"))

    @allure.step("Меняю валюту на {currency}")
    def change_currency(self, currency):
        self.logger.info(f"{self.class_name}: Change currency to {currency}")
        self.click((By.CSS_SELECTOR, "#form-currency"))
        self.click((By.CSS_SELECTOR, f"li > a[href='{currency}']"))
        self.get_element(
            (By.XPATH, f"//strong[text()='{CurrencySymbols.get_symbol(currency)}']")
        )
