import tkinter as tk
from tkinter import filedialog

def select_downloads_folder_manually():
    root = tk.Tk()
    root.withdraw()
    downloads_folder = filedialog.askdirectory(title="Select Downloads Folder")
    return downloads_folder
