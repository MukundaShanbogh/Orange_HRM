from config.config import Config
import pytest

def praser_adoption(praser):
    praser.addoption("--browser",
                     action="store",
                     default="chromium",
                     help="chromium, firefox or webkit")


@pytest.fixture(scope="session")
def pages(playwright,request):
    browser_type=request.config.getoption("--browser_type").lower()

    if browser_type == "webkit":
        browser_engine =playwright.webkit
    elif browser_type == "firefox":
        browser_engine =playwright.firefox
    else:
        browser_engine=playwright.chromium
    

    browser =browser_engine.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.Base_url)

    yield page

    context.close()
    browser.close()
