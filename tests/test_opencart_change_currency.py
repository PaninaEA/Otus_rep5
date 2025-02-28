import re
import pytest

from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage


@pytest.mark.parametrize(
    "request_currency, currency",
    [("EUR", "€"), ("USD", "$"), ("GBP", "£")],
)
def test_change_currency(browser, request_currency, currency):
    MainPage(browser).change_currency(request_currency)
    price_on_main_page = MainPage(browser).product_price().text
    price_in_cart = MainPage(browser).price_in_cart().text
    MainPage(browser).get_product_on_main_page().click()
    price_on_product_page = ProductPage(browser).price().text
    assert MainPage(browser).currency().text == currency, (
        "Валюта в меню на главной странице не изменилась"
    )
    assert re.search(currency, price_in_cart), "Валюта в корзине не изменилась"
    assert re.search(currency, price_on_main_page), (
        "Валюта в карточке товара на главной странице не изменилась"
    )
    assert re.search(currency, price_on_product_page), (
        "Валюта на странице товара не изменилась"
    )
