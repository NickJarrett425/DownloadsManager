import finder
import folders
import organizer
import platform
import selector

def main():
    downloads_folder = finder.find_downloads_folder()
    
    while not downloads_folder:
        print("Downloads folder not found for the current user.")
        print("Please select the downloads folder manually.")
        downloads_folder = selector.select_downloads_folder_manually()
    
    print("Downloads Folder Path:", downloads_folder)
    
    # Create Document folders
    document_folder = folders.create_document_subfolders(downloads_folder)
    if document_folder:
        print("Document Folder Path:", document_folder)
    else:
        print("Error creating document folders.")
    
    # Create Image folders
    image_folder = folders.create_image_subfolders(downloads_folder)
    if image_folder:
        print("Image Folder Path:", image_folder)
    else:
        print("Error creating image folders.")
    
    # Create Videos folder
    videos_folder = folders.create_videos_folder(downloads_folder)
    if videos_folder:
        print("Videos Folder Path:", videos_folder)
    else:
        print("Error creating Videos folder.")
    
    # Create Music folder
    music_folder = folders.create_music_folder(downloads_folder)
    if music_folder:
        print("Music Folder Path:", music_folder)
    else:
        print("Error creating Music folder.")
    
    # Create Archives folder
    archives_folder = folders.create_archives_folder(downloads_folder)
    if archives_folder:
        print("Archives Folder Path:", archives_folder)
    else:
        print("Error creating Archives folder.")
    
    # Create Software folder
    software_folder = folders.create_software_folder(downloads_folder)
    if software_folder:
        print("Software Folder Path:", software_folder)
    else:
        print("Error creating Software folder.")
    
    # Determine operating system
    os_system = platform.system()
    if os_system == "Windows":
        software_folders = organizer.windows_software
    elif os_system == "Darwin":  # macOS
        software_folders = organizer.mac_software
    elif os_system == "Linux":
        software_folders = organizer.linux_software
    else:
        print("Unknown operating system. Using default Windows software folder.")
        software_folders = organizer.windows_software
    
    # Create Miscellaneous folder
    miscellaneous_folder = folders.create_miscellaneous_folder(downloads_folder)
    if miscellaneous_folder:
        print("Miscellaneous Folder Path:", miscellaneous_folder)
    else:
        print("Error creating Miscellaneous folder.")
    
    # Call organizer script for each software folder dictionary
    for folders_dict in [organizer.document_folders, organizer.image_folders, organizer.video_folders, organizer.music_folders, organizer.archive_folders, software_folders]:
        organizer.organize_files(downloads_folder, folders_dict)
    
    # Delete empty folders
    folders.delete_empty_folders(downloads_folder)

if __name__ == "__main__":
    main()