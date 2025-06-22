from scrape_utils import scrape_and_screenshot

url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
text = scrape_and_screenshot(url)
print(text[:1000])  # Preview first 1000 characters
