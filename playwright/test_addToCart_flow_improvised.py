import time
from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("https://ohreems-automation-shop.netlify.app/")
    page.get_by_label("Username").fill("john")
    page.get_by_label("Password").fill("wick123")
    page.get_by_role("button", name="Login").click()
    time.sleep(3)


def add_product_to_cart(page: Page, product_name: str):
    product_card = page.locator(".card").filter(has_text=product_name)
    product_card.get_by_role("button", name="Add").click()


def verify_product_in_cart(page: Page, product_name: str):
    expect(page.locator("#cartTable")).to_contain_text(product_name)


def test_selectProducts(page: Page):

    # Login
    test_login(page)

    # Products to add
    products = [
        "Lenovo ThinkPad X1",
        "Acer Predator"
    ]

    # Add products
    for product in products:
        add_product_to_cart(page, product)

    # Open Cart
    page.get_by_role("button", name="View Cart").click()

    # Verify products in cart
    for product in products:
        verify_product_in_cart(page, product)

    # Verify total rows in cart
    expect(page.locator("#cartTable tr")).to_have_count(3)

    # Proceed to checkout
    page.get_by_role("button", name="Proceed to Checkout").click()