# 3. Import the requests library (already installed via pipenv)
import requests

# Make a GET request to Google's homepage
# (This is simpler than httpbin and more recognizable)
response = requests.get("https://www.google.com")

# Print the HTTP status code:
# 200 = success, 404 = not found, 500 = server error, etc.
print("Status Code:", response.status_code)

# Print the first 200 characters of the HTML content
# (The actual webpage content Google returns)
print("Content Preview:", response.text[:200])
