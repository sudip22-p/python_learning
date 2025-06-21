import os
import shutil

# Local source and destination folders
UN_ARRANGED_DIR = "./un_arranged_folder"
ARRANGED_DIR = "./arranged_folder"

# Define file type categories
EXTENSION_MAP = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "PDFs": [".pdf"],
    "Apps": [".exe", ".msi", ".apk", ".dmg"],
    "Docs": [".docx", ".txt", ".pptx", ".xlsx"],
    "Zips": [".zip", ".rar", ".7z", ".tar.gz"],
}


# Function to match extension to category
def get_category(ext):
    for category, extensions in EXTENSION_MAP.items():
        if ext.lower() in extensions:
            return category
    return "Others"


def organize_files():
    print(f"📁 Organizing from: {UN_ARRANGED_DIR} ➜ {ARRANGED_DIR}")
    os.makedirs(ARRANGED_DIR, exist_ok=True)

    for file in os.listdir(UN_ARRANGED_DIR):
        src_path = os.path.join(UN_ARRANGED_DIR, file)
        if os.path.isfile(src_path):
            ext = os.path.splitext(file)[1]
            category = get_category(ext)
            target_dir = os.path.join(ARRANGED_DIR, category)
            os.makedirs(target_dir, exist_ok=True)

            dest_path = os.path.join(target_dir, file)

            # ✅ COPY mode: keeps original file in source
            shutil.copy2(src_path, dest_path)
            print(f"📄 Copied: {file} ➜ {category}/")

            # ✅ MOVE mode (optional): uncomment this to move instead of copy
            # shutil.move(src_path, dest_path)
            # print(f"📄 Moved: {file} ➜ {category}/")

    print("✅ Organizing completed.")


if __name__ == "__main__":
    organize_files()
