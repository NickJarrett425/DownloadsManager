import os

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
