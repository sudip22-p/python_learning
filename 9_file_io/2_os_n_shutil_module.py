# Working with os and shutil modules
# These modules help with file system operations (e.g., renaming, removing, copying files and folders)
# ✅ Summary: shutil vs os for file and folder operations in Python

# 📁 Folder operations:

# os.mkdir("folder_name")           # Create a single folder
# os.makedirs("a/b/c", exist_ok=True)  # Create nested folders (no error if already exists)
# os.rmdir("folder_name")           # Remove EMPTY folder only
# shutil.rmtree("folder_name")      # Remove folder and ALL contents (non-empty too)

# 📄 File operations:

# os.rename("old.txt", "new.txt")   # Rename or move file/folder
# os.remove("file.txt")             # Delete a file
# shutil.copy("src.txt", "dst.txt") # Copy file
# shutil.move("src.txt", "dst.txt") # Move file (or folder)

# 🛠 Use os for:
# - Basic operations (create folder, delete file, rename)

# 🛠 Use shutil for:
# - High-level operations (copy, move, delete folders with contents)

# 🔐 Always use 'exist_ok=True' with os.makedirs() to avoid errors if folder exists
# ❗ Use shutil.rmtree() carefully — it deletes everything inside the folder


import os
import shutil

# Create a test directory
os.makedirs("test_folder", exist_ok=True)
os.makedirs("2_test_folder", exist_ok=True)
# Create a file inside it
with open("test_folder/sample.txt", "w") as f:
    f.write("Test file content")

# Copy the file to a new location
shutil.copy("test_folder/sample.txt", "copied_sample.txt")
shutil.copy("test_folder/sample.txt", "2_test_folder/copied_sample.txt")

# Rename the copied file
os.rename("copied_sample.txt", "renamed_sample.txt")

# Delete the copied file
os.remove("renamed_sample.txt")

# Remove the directory and its contents
shutil.rmtree("test_folder")
print("File and folder operations completed.")
