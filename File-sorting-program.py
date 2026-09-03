import os
import shutil
import tkinter
from tkinter import ttk

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
    moved_files = []

    for item in os.listdir(downloads_path):
        source = os.path.join(downloads_path, item)

        if os.path.isfile(source):
            filename_lower = item.lower()

            for keyword, folder_name in categories.items():
                if keyword in filename_lower:
                    destination = os.path.join(base_folder, folder_name, item)
                    shutil.move(source, destination)
                    moved_files.append(f"{item}  →  {folder_name}")
                    break


#GUI-----------------------------------------------------
#window
root = tkinter.Tk()
root.title('Python File Sorter')
root.geometry('500x400')
#freame
frm = ttk.Frame(root, padding=10)
frm.pack(fill='both', expand=True)

#Title
title = ttk.Label(frm, text='Classwork Sorting Program')
title.pack(pady=5)

#sort button
sort_button = ttk.Button(frm, text='Sort Files', command=sort_files)
sort_button.pack(pady=10)


root.mainloop()