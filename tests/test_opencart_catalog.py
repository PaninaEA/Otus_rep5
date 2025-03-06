import allure

from page_objects.catalog_page import CatalogPage


@allure.feature("Find elements")
@allure.story("Catalog page")
@allure.title("Elements on catalog page")
def test_find_elements(browser):
    CatalogPage(browser).open_desktops_catalog()
    CatalogPage(browser).current_menu_item
    CatalogPage(browser).compare_button
    CatalogPage(browser).sort_selection()
    CatalogPage(browser).product_card()


@allure.feature("Find elements")
@allure.story("Catalog page")
@allure.title("Number of desktops categories in catalog")
def test_number_of_desktops_categories(browser):
    CatalogPage(browser).open_desktops_catalog()
    assert len(CatalogPage(browser).categories_of_desktops()) == 2, (
        "В каталоге Desktops должно быть 2 категории"
    )
