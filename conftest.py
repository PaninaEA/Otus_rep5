import datetime
import logging

import allure
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", type=str, default="ch", help="Browser for tests")
    parser.addoption(
        "--base_url",
        type=str,
        default="http://192.168.0.105:8081",
        help="Base url for tests",
    )
    parser.addoption("--headless", action="store_true", default="true")
    parser.addoption(
        "--login:pwd", type=str, default="user:bitnami", help="login:password for admin"
    )
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != "passed":
        item.status = "failed"
    else:
        item.status = "passed"


@pytest.fixture
def browser(request):
    url = request.config.getoption("--base_url")
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    logger.setLevel(level=log_level)
    logger.info("===> Test started at %s" % datetime.datetime.now())
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
    driver.log_level = log_level
    driver.logger = logger
    driver.url = url
    driver.get(url)
    logger.info("Browser %s started" % browser)

    def fin():
        if request.node.status == "failed":
            allure.attach(
                name="failure_screenshot",
                body=driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG,
            )
        driver.quit()
        logger.info("===> Test finished at %s" % datetime.datetime.now())

    request.addfinalizer(fin)
    return driver


@pytest.fixture
def get_login_pass(request):
    return request.config.getoption("--login:pwd")
