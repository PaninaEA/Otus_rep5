import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_admin(browser, get_login, get_password):
    browser.get(browser.url + "/administration")
    wait = WebDriverWait(browser, 2)
    username = browser.find_element(By.CSS_SELECTOR, "#input-username.form-control")
    username.send_keys(get_login)
    password = browser.find_element(By.CSS_SELECTOR, "#input-password.form-control")
    password.send_keys(get_password)
    button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_submit.click()
    logout = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#nav-logout.nav-item"))
    )
    logout.click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-login")))


def test_cart_add(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 10)
    select_product = browser.find_element(
        By.CSS_SELECTOR, "div.product-thumb > div.content > div.description > h4 > a"
    )
    select_product.location_once_scrolled_into_view
    time.sleep(0.5)
    name_product = select_product.text
    product_add_cart = browser.find_element(
        By.CSS_SELECTOR, "button[formaction$='cart.add']"
    )
    product_add_cart.click()
    cart_button = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'1 item(s)')]")
        )
    )
    cart_button.location_once_scrolled_into_view
    wait.until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
        )
    )
    cart_button.click()
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, f"//td[@class='text-start']/a[text()='{name_product}']")
        )
    )


@pytest.mark.parametrize(
    "request_currency, currency",
    [("EUR", "€"), ("USD", "$"), ("GBP", "£")],
)
def test_change_currency(browser, request_currency, currency):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 3)
    menu_currency = browser.find_element(By.CSS_SELECTOR, "#form-currency")
    menu_currency.click()
    select_currency = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f"li > a[href='{request_currency}']")
        )
    )
    select_currency.click()
    wait.until(
        EC.visibility_of_element_located((By.XPATH, f"//strong[text()='{currency}']"))
    )
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, f"//span[contains(text(),'{currency}')]")
        )
    )
    catalog_products = browser.find_element(
        By.CSS_SELECTOR, "li.nav-item > a[href$='cameras']"
    )
    catalog_products.click()
    wait.until(EC.visibility_of_element_located((By.ID, "product-category")))
    browser.find_element(By.XPATH, f"//span[contains(text(),'{currency}')]")
