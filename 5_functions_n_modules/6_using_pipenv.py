# 1. Install requests package in current project
# pipenv install requests
"""
# terminal output:
------------------------------------------------------------------------------------------------------------------------------------
Creating a virtualenv for this project
Pipfile: /root/Docs/Python/learning/5_functions_n_modules/Pipfile
Using /usr/bin/python33.12.3 to create virtualenv...
⠼ Creating virtual environment...created virtual environment CPython3.12.3.final.0-64 in 259ms
  creator CPython3Posix(dest=/root/.local/share/virtualenvs/5_functions_n_modules-4lFc6FPP, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=/root/.local/share/virtualenv)
    added seed packages: pip==25.1.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /root/.local/share/virtualenvs/5_functions_n_modules-4lFc6FPP
Creating a Pipfile for this project...
Pipfile.lock not found, creating...
Locking  dependencies...
Locking  dependencies...
Updated Pipfile.lock (702ad05de9bc9de99a4807c8dde1686f31e0041d7b5f6f6b74861195a52110f5)!
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
Installing requests...
✔ Installation Succeeded
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
Installing dependencies from Pipfile.lock (2110f5)...
All dependencies are now up-to-date!
Upgrading requests in  dependencies.
Building requirements...
Resolving dependencies...
✔ Success!
Building requirements...
Resolving dependencies...
✔ Success!
Building requirements...
Resolving dependencies...
✔ Success!
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
Installing dependencies from Pipfile.lock (18b4fb)...
All dependencies are now up-to-date!
Installing dependencies from Pipfile.lock (18b4fb)...
------------------------------------------------------------------------------------------------------------------------------------
"""
# This will:
# - Create virtual environment (if none exists)
# - Install requests package + dependencies
# - Update Pipfile/Pipfile.lock

# 2. (Optional) Activate virtual environment
# pipenv shell
# Your terminal prompt will change showing virtualenv is active
# Now all commands use this environment's Python and packages
# Turns on your project’s private Python space.
# All commands now use your project’s Python and installed packages.
# Your prompt changes to show it’s active (e.g., (my_project-ABC123)).
"""

# Before: Uses system Python  
$ python --version  

# Activate  
$ pipenv shell  

# Now: Uses your project’s Python  
(my_project-ABC123) $ python --version  

"""
# installing package in virtual environment
"""

WHAT HAPPENS WHEN YOU RUN: pipenv install pandas

1. PROJECT SETUP
   - Looks for Pipfile (project config) in current folder
   - If no Pipfile exists, creates a new one automatically

2. VIRTUAL ENVIRONMENT
   - For first package install:
     • Creates isolated Python environment (hidden folder)
   - For existing projects:
     • Uses the already-created environment

3. PACKAGE INSTALLATION
   - Downloads pandas + all required dependencies
   - Installs them ONLY in this project's private space
   - Won't interfere with other projects or system Python

4. FILE UPDATES
   - Pipfile: Adds pandas to your package list
   - Pipfile.lock: Locks exact versions of:
     • pandas
     • All its dependencies
     • Their sub-dependencies

WHY THIS IS AWESOME:
✔ No more "it works on my machine" problems
✔ Each project gets its own clean package space
✔ Team members get identical environments

"""

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
