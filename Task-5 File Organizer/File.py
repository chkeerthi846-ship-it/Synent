import os
import shutil

# Set the folder you want to organize
folder_path = input("Enter folder path to organize: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"]
}

# Create folders if not exist
for category in file_types:
    category_path = os.path.join(folder_path, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# Organize files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, extension = os.path.splitext(file)

    moved = False
    for category, extensions in file_types.items():
        if extension.lower() in extensions:
            shutil.move(file_path, os.path.join(folder_path, category, file))
            moved = True
            break

    # If file type not matched
    if not moved:
        others_path = os.path.join(folder_path, "Others")
        if not os.path.exists(others_path):
            os.makedirs(others_path)
        shutil.move(file_path, os.path.join(others_path, file))

print("✅ Files organized successfully!")
