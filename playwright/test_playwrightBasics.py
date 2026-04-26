import time

from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
    # in one browser we can have multiple contexts,
    # in one context we can have multiple pages
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ohreems-automation-shop.netlify.app/")

#Chromium engine, headless mode , 1 single context
def test_playwrightShortcut(page:Page):
    page.goto("https://ohreems-automation-shop.netlify.app/")

def test_coreLocators(page:Page):
    page.goto("https://ohreems-automation-shop.netlify.app/")
    page.get_by_label("Username").fill("john")
    page.get_by_label("Password").fill("wick123")
    page.get_by_role("button", name="Login").click()
    time.sleep(5)

def test_switchTabs(page:Page):
    page.goto("https://ohreems-automation-shop.netlify.app/")

    # click "Forgot Password?" and wait for new tab to open
    #Listens for a new tab opening
    with page.context.expect_page() as new_page_info:
             page.get_by_role("link", name="Forgot Password?").click()

    #capture new page
    new_page = new_page_info.value

    # Wait for new tab to load
    new_page.wait_for_load_state()

    time.sleep(5)

    # Validate new page opened (optional)
    print("New Tab URL:", new_page.url)
    expect(page.locator("text=Forgot Password")).to_be_visible()

    # Switch back to original login page
    page.bring_to_front()

    # Validate we are back on login page
    expect(page.locator("text=Welcome to Ohreems Automation Shop")).to_be_visible()

    page.get_by_label("Username").fill("john")
    page.get_by_label("Password").fill("wick123")
    page.get_by_role("button", name="Login").click()
    time.sleep(5)
    page.get_by_role("link", name="Logout").click()
    expect(page.locator("text=Welcome to Ohreems Automation Shop")).to_be_visible()

def test_firefoxBrowser(playwright : Playwright):
        firefoxBrowser = playwright.firefox
        browser = firefoxBrowser.launch(headless=False)
        page = browser.new_page()
        page.goto("https://ohreems-automation-shop.netlify.app/")
        page.get_by_label("Username").fill("john")
        page.get_by_label("Password").fill("wick123")
        page.get_by_role("button", name="Login").click()
        time.sleep(5)
