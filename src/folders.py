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