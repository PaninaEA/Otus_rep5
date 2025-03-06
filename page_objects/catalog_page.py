import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    @allure.step("Открываю каталог Desktops")
    def open_desktops_catalog(self):
        self.logger.info(f"{self.class_name}: Open desktops catalog")
        self.click((By.CSS_SELECTOR, "li.nav-item.dropdown"))
        self.click((By.CSS_SELECTOR, "a.see-all[href$='desktops']"))

    @property
    @allure.step("Проверяю выбранный пункт Desktops в меню")
    def current_menu_item(self):
        self.logger.info(f"{self.class_name}: Find selected menu item")
        return self.get_element((By.CSS_SELECTOR, "a.list-group-item.active"))

    @property
    @allure.step("Ищу кнопку сравнения на странице")
    def compare_button(self):
        self.logger.info(f"{self.class_name}: Find compare button")
        return self.get_element((By.CSS_SELECTOR, "#compare-total"))

    @allure.step("Проверяю выбор вариатов сортировки")
    def sort_selection(self):
        self.logger.info(f"{self.class_name}: View the sorting option")
        sort_element = Select(self.get_element((By.CSS_SELECTOR, "select#input-sort")))
        sort_element.select_by_visible_text("Price (Low > High)")

    @allure.step("Ищу карточку продукта")
    def product_card(self):
        self.logger.info(f"{self.class_name}: Find product card")
        self.get_element((By.CSS_SELECTOR, "div.product-thumb"))

    @allure.step("Проверяю подкатегории каталога Desktops")
    def categories_of_desktops(self):
        self.logger.info(f"{self.class_name}: Find desktops categories")
        return self.get_elements(
            (By.CSS_SELECTOR, "div.list-group.mb-3 > a[href*='desktops/']")
        )
