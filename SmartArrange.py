import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Target folders based on file extensions
extension_folders = {
    '.pdf': 'PDF_Files',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.txt': 'Text_Files',
    '.docx': 'Word_Files',
    '.xlsx': 'Excel_Files',
    '.mp3': 'Music',
    '.mp4': 'Videos'
}

# File organizer function
def organize_files(folder_path):
    counter = 0
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            ext = ext.lower()

            if ext in extension_folders:
                target_folder = os.path.join(folder_path, extension_folders[ext])
                os.makedirs(target_folder, exist_ok=True)

                target_path = os.path.join(target_folder, file)
                shutil.move(file_path, target_path)
                counter += 1

    messagebox.showinfo("Operation Complete", f"{counter} files were successfully organized!")

# Folder selection function
def select_folder():
    folder_path = filedialog.askdirectory(title="Select a folder to organize")
    if folder_path:
        selected_folder.set(f"Selected folder: {folder_path}")
        organize_button.config(state="normal")
        organize_button.config(command=lambda: organize_files(folder_path))

# GUI setup
window = tk.Tk()
window.title("File Organizer")
window.iconbitmap("ikon.ico")
window.geometry("400x300")
window.configure(bg="#f2f2f2")

# Application title
title = tk.Label(window, text="📂 File Organizer", font=("Segoe UI", 16, "bold"), bg="#f2f2f2", fg="#333")
title.pack(pady=10)

# Description
description = tk.Label(window, text="Select a folder to automatically organize your files.", font=("Segoe UI", 10), bg="#f2f2f2")
description.pack()

# Display selected folder
selected_folder = tk.StringVar()
folder_label = tk.Label(window, textvariable=selected_folder, bg="#f2f2f2", fg="#007acc", wraplength=350)
folder_label.pack(pady=10)

# Select folder button
select_button = tk.Button(window, text="Select Folder", command=select_folder, font=("Segoe UI", 11), bg="#4CAF50", fg="white", padx=10, pady=5)
select_button.pack(pady=5)

# Start organizing button
organize_button = tk.Button(window, text="Start Organizing", font=("Segoe UI", 11), bg="#007acc", fg="white", padx=10, pady=5, state="disabled")
organize_button.pack(pady=10)

window.mainloop()
