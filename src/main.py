import finder
import folders

def main():
    downloads_folder = finder.find_downloads_folder()
    
    if downloads_folder:
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
        
        # Create Software folder
        software_folder = folders.create_software_folder(downloads_folder)
        if software_folder:
            print("Software Folder Path:", software_folder)
        else:
            print("Error creating Software folder.")
    else:
        print("Downloads folder not found for the current user.")
        print("Please select the downloads folder manually.")

if __name__ == "__main__":
    main()
