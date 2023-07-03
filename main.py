import os

def create_file(filename):
    with open(filename, 'w') as file:
        pass

def create_folder(foldername):
    os.makedirs(foldername, exist_ok=True)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("File not found.")

def delete_folder(foldername):
    if os.path.exists(foldername):
        os.rmdir(foldername)
    else:
        print("Folder not found.")

def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
    else:
        print("File not found.")

def edit_file(filename):
    if os.path.exists(filename):
        os.system(f"notepad {filename}")  # Open file in Notepad (Windows)
    else:
        print("File not found.")

def get_file_info(filename):
    if os.path.exists(filename):
        info = os.stat(filename)
        print(f"File: {filename}")
        print(f"Size: {info.st_size} bytes")
        print(f"Last modified: {info.st_mtime}")
    else:
        print("File not found.")

def get_folder_info(foldername):
    if os.path.exists(foldername):
        file_count = 0
        folder_count = 0
        total_size = 0
        for root, dirs, files in os.walk(foldername):
            file_count += len(files)
            folder_count += len(dirs)
            for file in files:
                total_size += os.path.getsize(os.path.join(root, file))

        print(f"Folder: {foldername}")
        print(f"Total files: {file_count}")
        print(f"Total folders: {folder_count}")
        print(f"Total size: {total_size} bytes")
    else:
        print("Folder not found.")

# Example usage
create_file("test.txt")
create_folder("data")
edit_file("test.txt")
get_file_info("test.txt")
get_folder_info("data")
rename_file("test.txt", "new_test.txt")
delete_file("new_test.txt")
delete_folder("data")
