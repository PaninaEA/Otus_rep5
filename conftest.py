from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", type=str, default="ch", help="Browser for tests")
    parser.addoption(
        "--base_url",
        type=str,
        default="http://192.168.0.112:8081",
        help="Base url for tests",
    )
    parser.addoption("--headless", action="store_true", default="true")
    parser.addoption(
        "--login:pwd", type=str, default="user:bitnami", help="login:password for admin"
    )


@pytest.fixture
def browser(request):
    url = request.config.getoption("--base_url")
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    if browser_name in ["chrome", "ch"]:
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name in ["yandex", "ya"]:
        options = webdriver.ChromeOptions()
        binary_yandex_driver_file = (
            "e:/drivers/yandexdriver.exe"  # path to YandexDriver
        )
        service = webdriver.chrome.service.Service(
            executable_path=binary_yandex_driver_file
        )
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    driver.url = url
    driver.get(url)
    return driver


@pytest.fixture
def get_login_pass(request):
    return request.config.getoption("--login:pwd")
