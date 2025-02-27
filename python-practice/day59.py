# Question: Day 59: Simple web scraper to extract headlines from news website.
import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return [h.text.strip() for h in soup.select('h2.headline')]

# Example usage (website structure may vary):
# print(scrape_headlines('https://example-news-site.com'))
