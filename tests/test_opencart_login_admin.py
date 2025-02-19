from selenium.webdriver.common.by import By


def test_find_elements(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(By.CSS_SELECTOR, "div.card-header")  # заголовок
    browser.find_element(
        By.CSS_SELECTOR, "div.card-body > form#form-login"
    )  # форма авторизации
    browser.find_element(
        By.CSS_SELECTOR, "#input-username.form-control"
    )  # поле для логина
    browser.find_element(
        By.CSS_SELECTOR, "#input-password.form-control"
    )  # поле для пароля
    browser.find_element(
        By.CSS_SELECTOR, "div.text-end button[type='submit']"
    )  # кнопка
    browser.find_element(By.CSS_SELECTOR, "footer#footer")  # футер
    assert browser.title == "Administration", "Неправильный заголовок страницы"
