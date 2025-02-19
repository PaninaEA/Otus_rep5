from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_elements(browser):
    browser.get(browser.url)
    browser.find_element(By.CSS_SELECTOR, "#search")  # строкa поиска
    browser.find_element(By.CSS_SELECTOR, "div#search button")  # кнопка поиска
    browser.find_element(
        By.CSS_SELECTOR, "div#header-cart button[type='button']"
    )  # корзина


def test_elements_menu(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.nav.navbar-nav")))
    menu_items = browser.find_elements(
        By.CSS_SELECTOR, "ul.nav.navbar-nav > li"
    )  # пункты меню
    assert len(menu_items) == 8, "В меню должно быть 8 пунктов"


def test_elements_dropdown_menu(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.nav.navbar-nav")))
    dropdown_menu = browser.find_elements(
        By.CSS_SELECTOR, "li.nav-item.dropdown"
    )  # выпадающие списки в меню
    assert len(dropdown_menu) == 4, "В меню должно быть 4 выпадающих списка"


def test_elements_menu_players(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 2)
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "li.nav-item.dropdown > a[href$='players']")
        )
    )
    dropdown_items_players = browser.find_elements(
        By.CSS_SELECTOR, "a[href*='players/']"
    )  # элементы подменю MP3 Players
    assert len(dropdown_items_players) == 18, (
        "Для MP3 Players должно быть 18 пунктов подменю"
    )
