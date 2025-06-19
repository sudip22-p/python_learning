import requests
from bs4 import BeautifulSoup

# URL of the static site
url = "http://books.toscrape.com/"  # This is a demo website for web scraping purposes.

# Send GET request to fetch the HTML content
response = requests.get(url)

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all book containers
books = soup.find_all("article", class_="product_pod")

# Loop over each book and extract title & price
for book in books[:10]:  # First 10 books
    # Title is inside <img> tag's title attribute
    title = book.find("h3").find("a")["title"]

    # Price is inside <p> tag with class 'price_color'
    price = book.find("p", class_="price_color").text

    print(f"{title} | {price}")
