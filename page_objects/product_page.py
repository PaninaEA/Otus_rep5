import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductPage(BasePage):
    @allure.step("Открываю страницу продукта {product_name}")
    def open_product_page(self, product_name):
        self.logger.info(f"{self.class_name}: Open page for product {product_name}")
        self.scroll_to_element(
            (
                By.CSS_SELECTOR,
                "div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4",
            )
        )
        self.click(
            (By.CSS_SELECTOR, f"div.description > h4 > a[href$='{product_name}']")
        )

    @property
    @allure.step("Получаю цену продукта")
    def price(self):
        self.logger.info(f"{self.class_name}: Find product price")
        return self.get_element((By.CSS_SELECTOR, "span.price-new"))

    @property
    @allure.step("Ищу кнопку добавления продукта в избранное")
    def add_wishlist_button(self):
        self.logger.info(f"{self.class_name}: Find button for add product in wishlist")
        return self.get_element((By.CSS_SELECTOR, "button[formaction$='wishlist.add']"))

    @property
    @allure.step("Ищу кнопку добавления продукта в корзину")
    def add_cart_button(self):
        self.logger.info(f"{self.class_name}: Find button for add product in cart")
        return self.get_element((By.CSS_SELECTOR, "#button-cart"))

    @property
    @allure.step("Ищу фото продукта")
    def product_foto(self):
        self.logger.info(f"{self.class_name}: Find product foto")
        return self.get_element(
            (By.CSS_SELECTOR, "div.image.magnific-popup img[src$='.jpg']")
        )

    @property
    @allure.step("Ищу открытую вкладку с описанием продукта")
    def active_tab_description(self):
        self.logger.info(f"{self.class_name}: Find product description")
        return self.get_element(
            (By.CSS_SELECTOR, "#tab-description.tab-pane.fade.show.active.mb-4")
        )

    @property
    @allure.step("Проверяю название страницы")
    def title(self):
        self.logger.info(f"{self.class_name}: Find page title")
        return self.browser.title

    @allure.step("Проверяю пункты в меню навигации")
    def navigation_items(self):
        self.logger.info(f"{self.class_name}: Find items in navigation menu")
        return self.get_elements(
            (By.CSS_SELECTOR, "li.breadcrumb-item > a[href^='http']")
        )
