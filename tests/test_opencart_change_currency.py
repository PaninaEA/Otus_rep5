import allure
from currency_symbols import CurrencySymbols
import re
import pytest

from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage


@pytest.mark.parametrize("currency", ["EUR", "USD", "GBP"])
@allure.feature("Actions")
@allure.story("Actions on main page")
@allure.title("Change currency to {currency} and check result")
def test_change_currency(browser, currency):
    MainPage(browser).change_currency(currency)
    currency_in_main_menu = MainPage(browser).currency.text
    price_on_main_page = MainPage(browser).product_price.text
    price_in_cart = MainPage(browser).price_in_cart.text
    MainPage(browser).click_product_on_main_page()
    price_on_product_page = ProductPage(browser).price.text
    assert currency_in_main_menu == CurrencySymbols.get_symbol(currency), (
        "Валюта в меню на главной странице не изменилась"
    )
    assert re.search(CurrencySymbols.get_symbol(currency), price_in_cart), (
        "Валюта в корзине не изменилась"
    )
    assert re.search(CurrencySymbols.get_symbol(currency), price_on_main_page), (
        "Валюта в карточке товара на главной странице не изменилась"
    )
    assert re.search(CurrencySymbols.get_symbol(currency), price_on_product_page), (
        "Валюта на странице товара не изменилась"
    )
