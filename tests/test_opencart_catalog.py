from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_find_elements(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 2)
    browser.find_element(
        By.CSS_SELECTOR, "div.list-group.mb-3 > a.list-group-item.active"
    )  # выбранный пункт меню
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#compare-total"))
    )  # кнопка сравнения
    sort_element = Select(
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "select#input-sort"))
        )
    )  # поле сортировки
    sort_element.select_by_visible_text(
        "Price (Low > High)"
    )  # один из вариантов сортировки
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-thumb"))
    )  # карточка товара


def test_catalog_menu(browser):
    wait = WebDriverWait(browser, 2)
    browser.get(browser.url + "/en-gb/catalog/component")
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.list-group.mb-3 > a[href$='component']")
        )
    )  # каталог components
    catalog_menu = browser.find_elements(
        By.CSS_SELECTOR, "div.list-group.mb-3 > a[href*='component/']"
    )  # подразделы каталога components
    assert len(catalog_menu) == 5, "В каталоге Components должно быть 5 пунктов"
