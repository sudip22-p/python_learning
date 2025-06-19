from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set headless Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome with WebDriverManager
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

# Navigate to a simple static site
driver.get("https://books.toscrape.com/")

# Wait for book elements to be visible
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.product_pod"))
)

# Extract and print first 10 book titles and prices
books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")[:10]
for book in books:
    title = book.find_element(By.TAG_NAME, "h3").text
    price = book.find_element(By.CLASS_NAME, "price_color").text
    print(f"{title} | {price}")

driver.quit()
