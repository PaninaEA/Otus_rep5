from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    def open_desktops_catalog(self):
        self.click((By.CSS_SELECTOR, "li.nav-item.dropdown"))
        self.click((By.CSS_SELECTOR, "a.see-all[href$='desktops']"))

    def current_menu_item(self):
        self.get_element((By.CSS_SELECTOR, "a.list-group-item.active"))

    def compare_button(self):
        self.get_element((By.CSS_SELECTOR, "#compare-total"))

    def sort_selection(self):
        sort_element = Select(self.get_element((By.CSS_SELECTOR, "select#input-sort")))
        sort_element.select_by_visible_text("Price (Low > High)")

    def product_card(self):
        self.get_element((By.CSS_SELECTOR, "div.product-thumb"))

    def categories_of_desktops(self):
        return self.get_elements(
            (By.CSS_SELECTOR, "div.list-group.mb-3 > a[href*='desktops/']")
        )
