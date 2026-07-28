# I hate this potato of a laptop
import os 
import shutil

#File sort
def sort_files():
    #Connects to downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    #Creates folder to sort into
    base_folder = os.path.join(downloads_path, "School2026")

    categories = {
        "english": "English",
        "math": "Math",
        "software": "Software",
        "outdoor": "Outdoor"
    }

    os.makedirs(base_folder, exist_ok=True)

    for folder in categories.values():
        os.makedirs(os.path.join(base_folder, folder), exist_ok=True)

    #Downloads folder check

sort_files()