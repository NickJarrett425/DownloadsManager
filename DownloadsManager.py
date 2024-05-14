import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox

def find_downloads_folder():
    # Get the user's home directory
    home_dir = os.path.expanduser("~")
    
    # Check if the downloads folder exists in the home directory
    downloads_folder = os.path.join(home_dir, "Downloads")
    
    # Check if the downloads folder exists and is a directory
    if os.path.exists(downloads_folder) and os.path.isdir(downloads_folder):
       return downloads_folder
    else:
        return None

def select_downloads_folder_manually():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Open a file dialog window to select the downloads folder
    downloads_folder = filedialog.askdirectory(title="Select Downloads Folder")
    
    return downloads_folder

def main():
    downloads_folder = find_downloads_folder()
    
    if downloads_folder:
        print("Downloads Folder Path:", downloads_folder)
    else:
        print("Downloads folder not found for the current user.")
        print("Please select the downloads folder manually.")
        
        # Show a notification message
        messagebox.showinfo("Select Downloads Folder", """Downloads folder not found. Please select the downloads folder manually.\n\nPress OK to continue.""")
        
        # Prompt the user to select the downloads folder manually
        downloads_folder = select_downloads_folder_manually()
        
        if downloads_folder:
            print("Selected Downloads Folder Path:", downloads_folder)
        else:
            print("No folder selected. Exiting.")

if __name__ == "__main__":
    main()
