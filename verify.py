from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{os.path.abspath('index.html')}")
    page.wait_for_timeout(2000)
    page.screenshot(path="screenshot.png", full_page=True)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
