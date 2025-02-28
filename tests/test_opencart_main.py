from page_objects.main_page import MainPage


def test_find_elements(browser):
    MainPage(browser).search_box()
    MainPage(browser).search_button()
    MainPage(browser).cart_button()


def test_number_of_menu_items(browser):
    assert len(MainPage(browser).menu_items()) == 8, "В меню должно быть 8 пунктов"


def test_number_of_dropdown_menu(browser):
    assert len(MainPage(browser).dropdown_menu()) == 4, (
        "В меню должно быть 4 выпадающих списка"
    )


def test_number_of_menu_players_items(browser):
    MainPage(browser).dropdown_menu_for_players()
    assert len(MainPage(browser).dropdown_menu_for_players()) == 18, (
        "Для MP3 Players должно быть 18 пунктов подменю"
    )


def test_add_product_to_cart(browser):
    MainPage(browser).add_product_to_cart()
