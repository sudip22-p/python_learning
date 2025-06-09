# ✅ Using external libraries in Python via pip

"""
External libraries are packages developed by others that you can use to add functionality.
Use pip (Python's package installer) to install them.

Install syntax:
    pip install <library-name>
Example:
    pip install requests

Best practice: Use a virtual environment (venv) to avoid global conflicts.

# ✅ Setting up virtual environment

For **Windows**:
    python -m venv venv
    venv\\Scripts\\activate

For **Linux**:
    python3 -m venv venv
    source venv/bin/activate

    # If venv is not found:
    sudo apt install python3-venv

Then install your library:
    pip install requests
"""

# ✅ Example: Using the 'requests' library

# Make sure you've installed the library using pip:
# Run this once in terminal: pip install requests

import requests  # External module for making HTTP requests

# Simple GET request to GitHub API
response = requests.get("https://api.github.com")

# Check if the request was successful (status code 200 = OK)
if response.status_code == 200:
    print("📡 Successfully connected to GitHub API")
    print("🔍 API Rate Limit Info:", response.headers["X-RateLimit-Limit"])
else:
    print("⚠️ Failed to connect:", response.status_code)
