import time

from playwright.sync_api import Page, expect, Playwright

def test_login(page: Page):
    page.goto("https://ohreems-automation-shop.netlify.app/")
    page.get_by_label("Username").fill("john")
    page.get_by_label("Password").fill("wick123")
    page.get_by_role("button", name="Login").click()
    time.sleep(3)

# Select 2 Products Lenovo ThinkPad X1 & Acer Predator
# Verify those products are added to cart
# Remove one product from cart and verify the other product is still in cart

def test_selectProducts(page : Page):
       # Select 2 Products Lenovo ThinkPad X1 & Acer Predator
       # call login method
        test_login(page)
        time.sleep(3)
        lenovoProduct = page.locator("div.card").filter(has_text="Lenovo ThinkPad X1")
        lenovoProduct.get_by_role("button", name="Add").click()
        acerProduct = page.locator("div.card").filter(has_text="Acer Predator")
        acerProduct.get_by_role("button", name="Add").click()
        time.sleep(5)
        page.get_by_text("View Cart").scroll_into_view_if_needed()
        page.get_by_text("View Cart").click()
        time.sleep(5)
        expect(page.locator("#cartTable")).to_contain_text("Lenovo ThinkPad X1")
        expect(page.locator("#cartTable")).to_contain_text("Acer Predator")
        page.get_by_role("button", name="Proceed to Checkout").first.click()
        time.sleep(5)