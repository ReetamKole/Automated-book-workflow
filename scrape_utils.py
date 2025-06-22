from playwright.sync_api import sync_playwright
import os

def scrape_and_screenshot(url, output_folder="output"):
    os.makedirs(output_folder, exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Screenshot
        screenshot_path = os.path.join(output_folder, "chapter.png")
        page.screenshot(path=screenshot_path, full_page=True)

        # Text scraping
        content = page.inner_text("div#mw-content-text")
        text_path = os.path.join(output_folder, "chapter.txt")
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(content)

        browser.close()
    return content
