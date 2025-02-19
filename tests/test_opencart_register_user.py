from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_elements(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(By.CSS_SELECTOR, "input#input-firstname.form-control")
    browser.find_element(By.CSS_SELECTOR, "input#input-lastname.form-control")
    browser.find_element(By.CSS_SELECTOR, "input#input-email.form-control")
    browser.find_element(By.CSS_SELECTOR, "input#input-password.form-control")
    browser.find_element(By.CSS_SELECTOR, "div.text-end > button[type='submit']")


def test_required_fields(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    required_fields = browser.find_elements(
        By.CSS_SELECTOR, "#form-register > fieldset > div.row.mb-3.required"
    )
    assert len(required_fields) == 4, "Должно быть 4 обязательных поля"


def test_menu_user(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 2)
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-right"))
    )  # меню пользователя
    user_menu_items = browser.find_elements(
        By.CSS_SELECTOR, "div > a.list-group-item"
    )  # пункты меню пользователя
    assert len(user_menu_items) == 13, "В меню должно быть 13 пунктов"
