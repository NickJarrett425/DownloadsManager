import os
import shutil
import tkinter as tk
from tkinter import simpledialog, ttk
import send2trash

def organize_pdf_files(downloads_folder):
    pdf_folder = os.path.join(downloads_folder, "Documents", "PDFs")
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    for root, dirs, files in os.walk(downloads_folder):
        # Exclude pdf_folder and its subfolders from the search
        if root.startswith(pdf_folder):
            continue

        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                destination_path = os.path.join(pdf_folder, file)
                if os.path.exists(destination_path):
                    choice = ask_user_decision(file)
                    if choice == "rename":
                        new_file_name = ask_user_new_name(file)
                        if new_file_name:
                            if not new_file_name.endswith(".pdf"):
                                new_file_name += ".pdf"
                            destination_path = os.path.join(pdf_folder, new_file_name)
                        else:
                            continue  # Skip moving the file if renaming is canceled
                    elif choice == "recycle":
                        send2trash.send2trash(pdf_path)
                        continue  # Move to the next file
                    elif choice == "skip":
                        continue  # Skip moving the file

                shutil.move(pdf_path, destination_path)

def ask_user_decision(file):
    root = tk.Tk()
    root.withdraw()
    dialog = DecisionDialog(root, file)
    root.wait_window(dialog)
    return dialog.choice

def ask_user_new_name(file):
    while True:
        new_name = simpledialog.askstring("Rename File", f"A file named '{file}' already exists in the destination folder. Please provide a new name:")
        if new_name is None:  # User clicked cancel
            return None
        if new_name.lower() == file.lower():
            tk.messagebox.showerror("Error", "You cannot use the same name as the original file.")
            continue
        if os.path.splitext(new_name)[0] == os.path.splitext(file)[0]:
            tk.messagebox.showerror("Error", "You cannot use the same name as the original file.")
            continue
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