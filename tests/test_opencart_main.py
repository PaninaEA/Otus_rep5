import allure

from page_objects.main_page import MainPage


@allure.feature("Find elements")
@allure.story("Main page")
@allure.title("Elements on main page")
def test_find_elements(browser):
    MainPage(browser).search_box
    MainPage(browser).search_button
    MainPage(browser).cart_button


@allure.feature("Find elements")
@allure.story("Admin page")
@allure.title("Number of main menu items")
def test_number_of_menu_items(browser):
    assert len(MainPage(browser).menu_items()) == 8, "В меню должно быть 8 пунктов"


@allure.feature("Find elements")
@allure.story("Admin page")
@allure.title("Number of drop-down lists in main menu")
def test_number_of_dropdown_menu(browser):
    assert len(MainPage(browser).dropdown_menu()) == 4, (
        "В меню должно быть 4 выпадающих списка"
    )


@allure.feature("Find elements")
@allure.story("Admin page")
@allure.title("Number of items in menu for MP3 Players")
def test_number_of_menu_players_items(browser):
    assert len(MainPage(browser).dropdown_menu_for_players()) == 18, (
        "Для MP3 Players должно быть 18 пунктов подменю"
    )


@allure.feature("Actions")
@allure.story("Actions on main page")
@allure.title("Add product to cart and check")
def test_add_product_to_cart(browser):
    product_to_add = MainPage(browser).add_product_to_cart()
    product_in_cart = MainPage(browser).get_product_in_cart()
    assert product_to_add == product_in_cart
