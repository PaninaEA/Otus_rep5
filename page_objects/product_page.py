from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductPage(BasePage):
    def open_product_page(self, product_name):
        self.click(
            (By.CSS_SELECTOR, f"div.description > h4 > a[href$='{product_name}']")
        )

    def price(self):
        return self.get_element((By.CSS_SELECTOR, "span.price-new"))

    def add_wishlist_button(self):
        self.get_element((By.CSS_SELECTOR, "button[formaction$='wishlist.add']"))

    def add_cart_button(self):
        self.get_element((By.CSS_SELECTOR, "#button-cart"))

    def product_foto(self):
        self.get_element((By.CSS_SELECTOR, "div.image.magnific-popup img[src$='.jpg']"))

    def active_tab_description(self):
        self.get_element(
            (By.CSS_SELECTOR, "#tab-description.tab-pane.fade.show.active.mb-4")
        )

    def title(self):
        return self.browser.title

    def navigation_items(self):
        return self.get_elements(
            (By.CSS_SELECTOR, "li.breadcrumb-item > a[href^='http']")
        )
