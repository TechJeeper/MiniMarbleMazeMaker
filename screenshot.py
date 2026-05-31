from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    pwd = os.getcwd()
    page.goto(f"file://{pwd}/index.html")
    page.wait_for_timeout(5000)
    page.screenshot(path="screenshot.png", full_page=True)
    browser.close()
