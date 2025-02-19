import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize(
    "request_product, product",
    [
        ("hp-lp3065", "HP LP3065"),
        ("apple-cinema", "Apple Cinema 30"),
        ("iphone", "iPhone"),
    ],
)
def test_find_elements(browser, request_product, product):
    browser.get(f"{browser.url}/en-gb/product/desktops/{request_product}")
    wait = WebDriverWait(browser, 2)
    browser.find_element(By.CSS_SELECTOR, "span.price-new")  # цена
    browser.find_element(
        By.CSS_SELECTOR, "button[formaction$='wishlist.add']"
    )  # кнопка - Добавить в избранное
    browser.find_element(By.CSS_SELECTOR, "#button-cart")  # кнопка - Добавить в корзину
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.image.magnific-popup img[src$='.jpg']")
        )
    )  # фото товара
    browser.find_element(
        By.CSS_SELECTOR, "#tab-description.tab-pane.fade.show.active.mb-4"
    )  # активная вкладка с описанием
    assert browser.title == product, "Неправильный заголовок страницы"


def test_element_navigation(browser):
    browser.get(browser.url + "/en-gb/product/desktops/iphone")
    navigation_item = browser.find_elements(
        By.CSS_SELECTOR, "li.breadcrumb-item > a[href^='http']"
    )  # ссылки в строке навигации
    assert len(navigation_item) == 3, "В строке навигации должно быть 3 пункта"
