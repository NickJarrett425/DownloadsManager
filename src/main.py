import finder
import selector
import tkinter.messagebox as messagebox

def main():
    downloads_folder = finder.find_downloads_folder()
    
    if downloads_folder:
        print("Downloads Folder Path:", downloads_folder)
    else:
        print("Downloads folder not found for the current user.")
        print("Please select the downloads folder manually.")
        
        messagebox.showinfo("Select Downloads Folder", "Downloads folder not found. Please select the downloads folder manually.")
        
        downloads_folder = selector.select_downloads_folder_manually()
        
        if downloads_folder:
            print("Selected Downloads Folder Path:", downloads_folder)
        else:
            print("No folder selected. Exiting.")

if __name__ == "__main__":
    main()
