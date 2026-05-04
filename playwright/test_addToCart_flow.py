import time
from playwright.sync_api import Page
from test_playwrightBasics import test_loginPage
from playwright.sync_api import Page, expect, Playwright



# Select 2 Products Lenovo ThinkPad X1 & Acer Predator
# Verify those products are added to cart
# Remove one product from cart and verify the other product is still in cart

def test_selectProducts(page : Page):
       # Select 2 Products Lenovo ThinkPad X1 & Acer Predator
       # call login method
        test_loginPage(page)
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


        page.get_by_role("button", name = "Back").click()

        time.sleep(5)

        page.locator("#categoryFilter").select_option("Furniture")

        products = ["Wooden Study Desk", "Modern Sofa Set"]

        for product in products:
                 product_card = page.locator("div.card").filter(has_text=product)
                 product_card.locator("input[type='number']").fill("3")
                 product_card.get_by_role("button", name="Add").click()



        page.get_by_text("View Cart").click()
        time.sleep(5)
        page.get_by_role("button", name="Proceed to Checkout").first.click()


