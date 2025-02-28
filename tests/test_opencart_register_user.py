import generate_data
from page_objects.user_page import UserPage


def test_number_of_required_fields(browser):
    UserPage(browser).open_register_user_page()
    assert len(UserPage(browser).required_fields()) == 4, (
        "Должно быть 4 обязательных поля"
    )


def test_number_of_menu_user_items(browser):
    UserPage(browser).open_register_user_page()
    assert len(UserPage(browser).user_menu_items()) == 13, (
        "В меню должно быть 13 пунктов"
    )


def test_register_new_user(browser):
    UserPage(browser).open_register_user_page()
    UserPage(browser).register_new_user(generate_data.create_user())
