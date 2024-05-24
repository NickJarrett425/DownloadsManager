import os
import platform

def create_document_subfolders(downloads_folder):
    document_folder = os.path.join(downloads_folder, "Documents")
    document_subfolders = ["PDFs", "Word Documents", "Spreadsheets", "Presentations", "Text Files"]
    
    # Check if the Documents folder already exists
    if os.path.exists(document_folder):
        print("Documents folder already exists. Adding subfolders if needed.")
    else:
        try:
            # Create the Documents folder
            os.makedirs(document_folder)
            print("Documents folder created.")
        except Exception as e:
            print(f"An error occurred while creating Documents folder: {str(e)}")
            return None

    # Add subfolders to the Documents folder
    for subfolder in document_subfolders:
        subfolder_path = os.path.join(document_folder, subfolder)
        if not os.path.exists(subfolder_path):
            try:
                # Create subfolders if they don't exist
                os.makedirs(subfolder_path)
                print(f"Subfolder '{subfolder}' created.")
            except Exception as e:
                print(f"An error occurred while creating subfolder '{subfolder}': {str(e)}")
        else:
            print(f"Subfolder '{subfolder}' already exists. Skipping.")

    return document_folder

def create_image_subfolders(downloads_folder):
    image_folder = os.path.join(downloads_folder, "Images")
    image_subfolders = ["Pictures", "GIFs", "Photoshop Documents"]
    
    # Check if the Images folder already exists
    if os.path.exists(image_folder):
        print("Images folder already exists. Adding subfolders if needed.")
    else:
        try:
            # Create the Images folder
            os.makedirs(image_folder)
            print("Images folder created.")
        except Exception as e:
            print(f"An error occurred while creating Images folder: {str(e)}")
            return None

    # Add subfolders to the Images folder
    for subfolder in image_subfolders:
        subfolder_path = os.path.join(image_folder, subfolder)
        if not os.path.exists(subfolder_path):
            try:
                # Create subfolders if they don't exist
                os.makedirs(subfolder_path)
                print(f"Subfolder '{subfolder}' created.")
            except Exception as e:
                print(f"An error occurred while creating subfolder '{subfolder}': {str(e)}")
        else:
            print(f"Subfolder '{subfolder}' already exists. Skipping.")
import os

def create_document_subfolders(downloads_folder):
    document_folder = os.path.join(downloads_folder, "Documents")
    document_subfolders = ["PDFs", "Word Documents", "Spreadsheets", "Presentations", "Text Files"]
    
    # Check if the Documents folder already exists
    if os.path.exists(document_folder):
        print("Documents folder already exists. Adding subfolders if needed.")
    else:
        try:
            # Create the Documents folder
            os.makedirs(document_folder)
            print("Documents folder created.")
        except Exception as e:
            print(f"An error occurred while creating Documents folder: {str(e)}")
            return None

    # Add subfolders to the Documents folder
    for subfolder in document_subfolders:
        subfolder_path = os.path.join(document_folder, subfolder)
        if not os.path.exists(subfolder_path):
            try:
                # Create subfolders if they don't exist
                os.makedirs(subfolder_path)
                print(f"Subfolder '{subfolder}' created.")
            except Exception as e:
                print(f"An error occurred while creating subfolder '{subfolder}': {str(e)}")
        else:
            print(f"Subfolder '{subfolder}' already exists. Skipping.")

    return document_folder

def create_image_subfolders(downloads_folder):
    image_folder = os.path.join(downloads_folder, "Images")
    image_subfolders = ["Pictures", "GIFs", "Photoshop Documents"]
    
    # Check if the Images folder already exists
    if os.path.exists(image_folder):
        print("Images folder already exists. Adding subfolders if needed.")
    else:
        try:
            # Create the Images folder
            os.makedirs(image_folder)
            print("Images folder created.")
        except Exception as e:
            print(f"An error occurred while creating Images folder: {str(e)}")
            return None

    # Add subfolders to the Images folder
    for subfolder in image_subfolders:
        subfolder_path = os.path.join(image_folder, subfolder)
        if not os.path.exists(subfolder_path):
            try:
                # Create subfolders if they don't exist
                os.makedirs(subfolder_path)
                print(f"Subfolder '{subfolder}' created.")
            except Exception as e:
                print(f"An error occurred while creating subfolder '{subfolder}': {str(e)}")
        else:
            print(f"Subfolder '{subfolder}' already exists. Skipping.")

    return image_folder

def create_videos_folder(downloads_folder):
    videos_folder = os.path.join(downloads_folder, "Videos")
    
    # Check if the Videos folder already exists
    if os.path.exists(videos_folder):
        print("Videos folder already exists.")
        return videos_folder
    else:
        try:
            # Create the Videos folder
            os.makedirs(videos_folder)
            print("Videos folder created.")
            return videos_folder
        except Exception as e:
            print(f"An error occurred while creating Videos folder: {str(e)}")
            return None

def create_music_folder(downloads_folder):
    music_folder = os.path.join(downloads_folder, "Music")
    
    # Check if the Music folder already exists
    if os.path.exists(music_folder):
        print("Music folder already exists.")
        return music_folder
    else:
        try:
            # Create the Music folder
            os.makedirs(music_folder)
            print("Music folder created.")
            return music_folder
        except Exception as e:
            print(f"An error occurred while creating Music folder: {str(e)}")
            return None

    return image_folder

def create_videos_folder(downloads_folder):
    videos_folder = os.path.join(downloads_folder, "Videos")
    
    # Check if the Videos folder already exists
    if os.path.exists(videos_folder):
        print("Videos folder already exists.")
        return videos_folder
    else:
        try:
            # Create the Videos folder
            os.makedirs(videos_folder)
            print("Videos folder created.")
            return videos_folder
        except Exception as e:
            print(f"An error occurred while creating Videos folder: {str(e)}")
            return None
        
def create_software_folder(downloads_folder):
    software_folder = os.path.join(downloads_folder, "Software")
    
    # Check if the Software folder already exists
    if os.path.exists(software_folder):
        print("Software folder already exists.")
        return software_folder
    else:
        try:
            # Create the Software folder
            os.makedirs(software_folder)
            print("Software folder created.")
        except Exception as e:
            print(f"An error occurred while creating Software folder: {str(e)}")
            return None
    
    # Determine operating system and create appropriate subfolders
    system = platform.system()
    subfolders = []

    if system == "Windows":
        subfolders = ["Executables", "Installers", "Batch Files", "Java Files", "Python Files"]
    elif system == "Darwin":  # macOS
        subfolders = ["Disk Images", "Applications", "Java Files", "Python Files"]
    elif system == "Linux":
        subfolders = ["Debian Packages", "RPM Packages", "Shell Scripts", "Java Files", "Python Files"]

    # Add subfolders to the Software folder
    for subfolder in subfolders:
        subfolder_path = os.path.join(software_folder, subfolder)
        if not os.path.exists(subfolder_path):
            try:
                # Create subfolders if they don't exist
                os.makedirs(subfolder_path)
                print(f"Subfolder '{subfolder}' created.")
            except Exception as e:
                print(f"An error occurred while creating subfolder '{subfolder}': {str(e)}")
        else:
            print(f"Subfolder '{subfolder}' already exists. Skipping.")

    return software_folder

def create_archives_folder(downloads_folder):
    archives_folder = os.path.join(downloads_folder, "Archives")
    archives_subfolders = ["Archives", "Compressed Files", "Disk Images"]
    
    # Check if the Archives folder already exists
    if os.path.exists(archives_folder):
        print("Archives folder already exists. Adding subfolders if needed.")
    else:
        try:
            # Create the Archives folder
            os.makedirs(archives_folder)
            print("Archives folder created.")
        except Exception as e:
            print(f"An error occurred while creating Archives folder: {str(e)}")
            return None

    # Add subfolders to the Archives folder
    for subfolder in archives_subfolders:
        subfolder_path = os.path.join(archives_folder, subfolder)
        if not os.path.exists(subfolder_path):
            try:
                # Create subfolders if they don't exist
                os.makedirs(subfolder_path)
                print(f"Subfolder '{subfolder}' created.")
            except Exception as e:
                print(f"An error occurred while creating subfolder '{subfolder}': {str(e)}")
        else:
            print(f"Subfolder '{subfolder}' already exists. Skipping.")

    return archives_folder

def create_miscellaneous_folder(downloads_folder):
    miscellaneous_folder = os.path.join(downloads_folder, "Miscellaneous")
    
    # Check if the Miscellaneous folder already exists
    if os.path.exists(miscellaneous_folder):
        print("Miscellaneous folder already exists.")
        return miscellaneous_folder
    else:
        try:
            # Create the Miscellaneous folder
            os.makedirs(miscellaneous_folder)
            print("Miscellaneous folder created.")
            return miscellaneous_folder
        except Exception as e:
            print(f"An error occurred while creating Miscellaneous folder: {str(e)}")
            return None
        
def delete_empty_folders(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):  # Check if the directory is empty
                os.rmdir(dir_path)