# ✅ Real-life recursion: Navigating nested folders (like a file explorer)


# Recursive function to print all folders and sub folders
def print_folders(folder):
    # Print the current folder's name
    print(f"📁 {folder['name']}")

    # Check if this folder has sub folders
    for subfolder in folder.get("subfolders", []):
        """
        If the key "subfolders" exists, it returns the list of subfolders.
        If "subfolders" doesn't exist, it returns an empty list [] (so the loop just skips).
        """
        # 🔁 Recursively call the function for each subfolder
        # This means: go one level deeper and repeat the same steps
        print_folders(subfolder)


# Simulated folder structure as a nested dictionary
folders = {
    "name": "Root",  # Main root folder
    "subfolders": [
        {"name": "Documents"},  # A single-level folder
        {
            "name": "Projects",  # Has more folders inside it (i.e., nested)
            "subfolders": [
                {"name": "Python"},
                {"name": "Web"},
            ],
        },
        {"name": "Images"},
    ],
}

# Start printing from the root folder
print_folders(folders)
