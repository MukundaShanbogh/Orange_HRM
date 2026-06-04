from config.config import Config
import pytest

@pytest.fixture(scope="session")
def pages(playwright):
    browser =playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(Config.Base_url)

    yield page

    context.close()
    browser.close()
