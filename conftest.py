from config.config import Config


def pages(playwright):
    browser =playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    page.goto(Config.Base_url)
