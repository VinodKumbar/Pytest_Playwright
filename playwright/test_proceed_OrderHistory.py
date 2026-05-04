
from test_playwrightBasics import test_loginPage
from test_addToCart_flow import test_selectProducts
from playwright.sync_api import Page, expect, Playwright


def test_orderHistory(page: Page):
         test_loginPage(page)
         page.wait_for_timeout(3000)
         test_selectProducts(page)
         page.wait_for_timeout(3000)

         page.get_by_placeholder("Full Name").fill("John Wick")
         page.locator("#address").fill("123 Main St, Apt 4New York, NY 10001USA")
         page.locator("#country").select_option("USA")
         page.locator("#state").select_option("Texas")
         page.get_by_text("Card").click()
         page.locator("#agreePolicy").click()
         page.get_by_role("button", name="Place Order").click()
         page.wait_for_timeout(3000)
         order_id = page.locator("#orderId").inner_text()
         assert order_id != ""
         print(order_id)
         page.wait_for_timeout(3000)
         page.get_by_role("button", name="Continue Shopping").click()
         page.wait_for_timeout(3000)
         page.get_by_role("button", name="Order History").click()
         page.wait_for_timeout(5000)
         expect(page.locator("#orderTable")).to_be_visible()
         page.get_by_role("button", name="Delete All Orders").click()
         page.wait_for_timeout(3000)
         page.get_by_role("button", name="Logout").click()
         page.wait_for_timeout(3000)
         expect(page.locator("text=Welcome to Ohreems Automation Shop")).to_be_visible()
