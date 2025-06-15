import requests  # External module for making HTTP requests

# Simple GET request to GitHub API
response = requests.get("https://api.github.com")

# Check if the request was successful (status code 200 = OK)
if response.status_code == 200:
    print("📡 Successfully connected to GitHub API")
    print("🔍 API Rate Limit Info:", response.headers["X-RateLimit-Limit"])
else:
    print("⚠️ Failed to connect:", response.status_code)
