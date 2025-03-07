import allure
import pytest
from page_objects.product_page import ProductPage


@allure.feature("Find elements")
@allure.story("Product page")
@allure.title("Elements on product page")
@pytest.mark.parametrize(
    "request_product, product",
    [
        ("macbook", "MacBook"),
        ("apple-cinema", "Apple Cinema 30"),
        ("iphone", "iPhone"),
    ],
)
def test_elements_on_product_page(browser, request_product, product):
    ProductPage(browser).open_product_page(request_product)
    ProductPage(browser).price
    ProductPage(browser).add_wishlist_button
    ProductPage(browser).add_cart_button
    ProductPage(browser).product_foto
    ProductPage(browser).active_tab_description
    assert ProductPage(browser).title == product, "Неправильный заголовок страницы"
    assert len(ProductPage(browser).navigation_items()) == 2, (
        "В строке навигации должно быть 2 пункта"
    )
