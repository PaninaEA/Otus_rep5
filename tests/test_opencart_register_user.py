import allure

import generate_data
from page_objects.user_page import UserPage


@allure.feature("Find elements")
@allure.story("User page")
@allure.title("Number of required fields on register user page")
def test_number_of_required_fields(browser):
    UserPage(browser).open_register_user_page()
    assert len(UserPage(browser).required_fields()) == 4, (
        "Должно быть 4 обязательных поля"
    )


@allure.feature("Find elements")
@allure.story("User page")
@allure.title("Number of items in user menu")
def test_number_of_menu_user_items(browser):
    UserPage(browser).open_register_user_page()
    assert len(UserPage(browser).user_menu_items()) == 13, (
        "В меню должно быть 13 пунктов"
    )


@allure.feature("Actions")
@allure.story("Actions on user page")
@allure.title("Register new user")
def test_register_new_user(browser):
    UserPage(browser).open_register_user_page()
    UserPage(browser).register_new_user(generate_data.create_user())
