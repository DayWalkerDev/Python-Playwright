from playwright.sync_api import sync_playwright

with sync_playwright() as pl:
    browser = pl.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.dianosprints.com")
    print(page.title())
    browser.close()
