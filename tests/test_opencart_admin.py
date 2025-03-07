import allure

import generate_data
from page_objects.admin_page import AdminPage


@allure.feature("Find elements")
@allure.story("Admin page")
@allure.title("Elements on admin page")
def test_elements_on_login_admin_page(browser):
    AdminPage(browser).open_admin_page()
    AdminPage(browser).header
    AdminPage(browser).form_login
    AdminPage(browser).footer
    assert AdminPage(browser).title == "Administration", (
        "Неправильный заголовок страницы"
    )


@allure.feature("Authorization")
@allure.story("Login")
@allure.title("Login on admin page")
def test_login(browser, get_login_pass):
    AdminPage(browser).open_admin_page()
    AdminPage(browser).login(get_login_pass)


@allure.feature("Authorization")
@allure.story("Logout")
@allure.title("Logout on admin page")
def test_logout(browser, get_login_pass):
    AdminPage(browser).open_admin_page()
    AdminPage(browser).login(get_login_pass)
    AdminPage(browser).logout()


@allure.feature("Actions")
@allure.story("Actions on admin page")
@allure.title("Add new product and delete")
def test_add_and_delete_product(browser, get_login_pass):
    new_product = generate_data.create_product()
    AdminPage(browser).open_admin_page()
    AdminPage(browser).login(get_login_pass)
    AdminPage(browser).open_products()
    AdminPage(browser).add_new_product(new_product)
    find_new_product = AdminPage(browser).find_product(new_product["product_name"])
    AdminPage(browser).delete_product()
    find_delete_product = AdminPage(browser).find_product(new_product["product_name"])
    assert find_new_product, "Новый товар не был добавлен"
    assert not find_delete_product, "Товар не был удален"
