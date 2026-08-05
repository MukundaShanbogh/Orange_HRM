import pytest

from config.config import Config



def pytest_addoption(parser):
    parser.addoption("--browser_type",
                     action="store",
                     default="chromium",
                     help="chromium, firefox or webkit")


@pytest.fixture(scope="function")
def pages(playwright,request):
    browser_type=request.config.getoption("--browser_type").lower()

    if browser_type == "webkit":
        browser_engine =playwright.webkit
    elif browser_type == "firefox":
        browser_engine =playwright.firefox
    else:
        browser_engine=playwright.chromium
    

    browser =browser_engine.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.Base_url)

    yield page

    context.close()
    browser.close()
