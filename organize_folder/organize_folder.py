import os
import shutil

def get_downloads_folder():
    return os.path.expanduser(r'C:\\Users\\Roshan George\\Downloads')

def list_files_in_folder(path):
    return os.listdir(path)

def create_folder(file, download_folder):
    file_path = os.path.join(download_folder, file)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1][1:]
        new_folder = os.path.join(download_folder, file_ext)
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        return new_folder
    
def move_files(file, folder):
    shutil.move(file, folder)

def main():
    downloads_folder = get_downloads_folder()
    files = list_files_in_folder(downloads_folder)
    for file in files:
        new_folder = create_folder(file, downloads_folder)
        if new_folder:
            move_files(os.path.join(downloads_folder, file), new_folder)

if __name__ == "__main__":
    main()