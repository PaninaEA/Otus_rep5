import datetime
import logging

import allure
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", type=str, default="chrome", help="Browser for tests")
    parser.addoption("--ver", help="Browser version for tests")
    parser.addoption(
        "--base_url",
        type=str,
        default="http://192.168.0.104:8081",
        help="Base url for tests",
    )
    parser.addoption("--headless", action="store_true", default="true")
    parser.addoption(
        "--login:pwd", type=str, default="user:bitnami", help="login:password for admin"
    )
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="192.168.0.104")
    parser.addoption("--logs", action="store_true")


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
    ver = request.config.getoption("--ver")
    executor = request.config.getoption("--executor")
    logs = request.config.getoption("--logs")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    logger.setLevel(level=log_level)
    logger.info("===> Test started at %s" % datetime.datetime.now())
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
    elif browser_name == "MicrosoftEdge":
        options = webdriver.EdgeOptions()
    options.set_capability("browserName", browser_name)
    options.set_capability("browserVersion", ver)
    options.set_capability(
        "selenoid:options",
        {"name": request.node.name, "enableLogs": logs, "enableVNC": True},
    )
    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub", options=options
    )
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
