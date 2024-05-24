import os
import shutil
import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
import send2trash

document_folders = {
    "PDFs": [".pdf"],
    "Word Documents": [".docx", ".doc", ".rtf"],
    "Spreadsheets": [".xlsx", ".xls", ".csv", ".xlsm"],
    "Presentations": [".pptx", ".ppt"],
    "Text Files": [".txt"]
}

image_folders = {
    "Pictures": [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".svg"],
    "GIFs": [".gif"],
    "Photoshop Documents": [".psd"]
}

video_folders = {
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"]
}

music_folders = {
    "Music": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".wma"]
}

archive_folders = {
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Compressed Files": [".gz", ".bz2"],
    "Disk Images": [".iso"]
}

windows_software = {
    "Executables": [".exe"],
    "Installers": [".msi"],
    "Batch Files": [".bat"],
    "Java Files": [".jar"],
    "Python Files": [".py"]
}

mac_software = {
    "Disk Images": [".dmg"],
    "Applications": [".app"],
    "Java Files": [".jar"],
    "Python Files": [".py"]
}

linux_software = {
    "Debian Packages": [".deb"],
    "RPM Packages": [".rpm"],
    "Shell Scripts": [".sh"],
    "Java Files": [".jar"],
    "Python Files": [".py"]
}

def organize_files(downloads_folder, folders_dict):
    if folders_dict is document_folders:
        base_folder = "Documents"
    elif folders_dict is image_folders:
        base_folder = "Images"
    elif folders_dict is video_folders:
        base_folder = "Videos"
    elif folders_dict is music_folders:
        base_folder = "Music"
    elif folders_dict is archive_folders:
        base_folder = "Archives"
    elif folders_dict is windows_software or folders_dict is mac_software or folders_dict is linux_software:
        base_folder = "Software"
    else:
        base_folder = "Miscellaneous"

    for folder_name, extensions in folders_dict.items():
        # For Videos and Music, don't create a subfolder named the same as the base folder
        if base_folder in ["Videos", "Music"]:
            folder_path = os.path.join(downloads_folder, base_folder)
        else:
            folder_path = os.path.join(downloads_folder, base_folder, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for root, dirs, files in os.walk(downloads_folder):
            if root.startswith(folder_path):
                continue

            for file in files:
                file_extension = os.path.splitext(file)[1].lower()
                if any(file_extension == ext for ext in extensions):
                    file_path = os.path.join(root, file)
                    destination_path = os.path.join(folder_path, file)
                    if os.path.exists(destination_path):
                        choice = ask_user_decision(file)
                        if choice == "rename":
                            new_file_name = ask_user_new_name(file, extensions)
                            if new_file_name:
                                destination_path = os.path.join(folder_path, new_file_name)
                            else:
                                continue  # Skip moving the file if renaming is canceled
                        elif choice == "recycle":
                            send2trash.send2trash(file_path)
                            continue  # Move to the next file
                        elif choice == "skip":
                            continue  # Skip moving the file

                    shutil.move(file_path, destination_path)

    # Handle files with extensions not found in any dictionary
    for root, dirs, files in os.walk(downloads_folder):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            if not any(file_extension in ext_list for ext_dict in [document_folders, image_folders, video_folders, music_folders, archive_folders, windows_software, mac_software, linux_software] for ext_list in ext_dict.values()):
                misc_folder_path = os.path.join(downloads_folder, "Miscellaneous")
                if root.startswith(misc_folder_path):
                    continue  # Skip files already in the Miscellaneous folder

                if not os.path.exists(misc_folder_path):
                    os.makedirs(misc_folder_path)
                file_path = os.path.join(root, file)
                destination_path = os.path.join(misc_folder_path, file)
                if os.path.exists(destination_path):
                    choice = ask_user_decision(file)
                    if choice == "rename":
                        new_file_name = ask_user_new_name(file, [])
                        if new_file_name:
                            destination_path = os.path.join(misc_folder_path, new_file_name)
                        else:
                            continue  # Skip moving the file if renaming is canceled
                    elif choice == "recycle":
                        send2trash.send2trash(file_path)
                        continue  # Move to the next file
                    elif choice == "skip":
                        continue  # Skip moving the file

                shutil.move(file_path, destination_path)

def ask_user_decision(file):
    root = tk.Tk()
    root.withdraw()
    dialog = DecisionDialog(root, file)
    root.wait_window(dialog)
    return dialog.choice

def ask_user_new_name(file, extensions):
    while True:
        new_name = simpledialog.askstring("Rename File", f"A file named '{file}' already exists in the destination folder. Please provide a new name:")
        if new_name is None:  # User clicked cancel
            return None
        original_name_without_ext = os.path.splitext(file)[0].lower()
        new_name_without_ext = os.path.splitext(new_name)[0].lower()
        if new_name_without_ext == original_name_without_ext:
            messagebox.showerror("Error", "You cannot use the same name as the original file.")
            continue
        # Check if the new name already has an extension
        if not any(new_name.lower().endswith(ext) for ext in extensions):
            # Add the correct extension if missing
            if extensions:
                new_name += extensions[0]
            else:
                _, ext = os.path.splitext(file)
                new_name += ext
        return new_name

class DecisionDialog(tk.Toplevel):
    def __init__(self, parent, filename):
        super().__init__(parent)
        self.filename = filename
        self.title("File Conflict")
        self.choice = None

        self.protocol("WM_DELETE_WINDOW", self.skip)

        self.label = ttk.Label(self, text=f"A file named '{filename}' already exists in the destination folder.\nWhat would you like to do?")
        self.label.pack(pady=10, padx=20)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=(0, 10))

        self.rename_button = ttk.Button(self.button_frame, text="Rename", command=self.rename)
        self.rename_button.pack(side=tk.LEFT, padx=10)

        self.recycle_button = ttk.Button(self.button_frame, text="Recycle", command=self.recycle)
        self.recycle_button.pack(side=tk.LEFT, padx=10)

        self.skip_button = ttk.Button(self.button_frame, text="Skip", command=self.skip)
        self.skip_button.pack(side=tk.LEFT, padx=10)

        # Center the dialog on the screen
        self.update_idletasks()
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')

    def rename(self):
        self.choice = "rename"
        self.destroy()

    def recycle(self):
        self.choice = "recycle"
        self.destroy()

    def skip(self):
        self.choice = "skip"
        self.destroy()
