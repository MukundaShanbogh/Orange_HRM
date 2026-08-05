import os
import pytest
import allure
from config.config import Config

# 1. Ensure the screenshots directory exists before tests start
SCREENSHOT_DIR = os.path.join(os.getcwd(), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# 2. Your custom command line option for browser selection
def pytest_addoption(parser):
    parser.addoption("--browser_type",
                     action="store",
                     default="chromium",
                     help="chromium, firefox or webkit")

# 3. Hook to track pass/fail status of tests
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# 4. Session-scoped Browser (Launches once per worker for speed)
@pytest.fixture(scope="session")
def custom_browser(playwright, request):
    browser_type = request.config.getoption("--browser_type").lower()

    if browser_type == "webkit":
        browser_engine = playwright.webkit
    elif browser_type == "firefox":
        browser_engine = playwright.firefox
    else:
        browser_engine = playwright.chromium
    
    browser = browser_engine.launch(headless=True)
    yield browser
    browser.close()

# 5. Function-scoped Page with Local Save + Allure Attach
@pytest.fixture(scope="function")
def pages(custom_browser, request):
    # Contexts are isolated (no shared cookies/cache between tests)
    context = custom_browser.new_context()
    page = context.new_page()
    page.goto(Config.Base_url)

    yield page

    # 6. Check if the test failed during execution ("call" phase)
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        # Create a safe file path using the test name
        file_name = f"{request.node.name}.png"
        file_path = os.path.join(SCREENSHOT_DIR, file_name)
        
        # Taking the screenshot with 'path' saves it to your physical folder.
        # It ALSO returns the bytes, which we catch in the variable below.
        screenshot_bytes = page.screenshot(path=file_path, full_page=True)
        
        # Attach those exact bytes directly to the Allure report
        allure.attach(
            screenshot_bytes, 
            name=f"Failed: {request.node.name}", 
            attachment_type=allure.attachment_type.PNG
        )

    context.close()