import os
import shutil

def show_files(path):
    print("\nFiles and Folders:")
    for item in os.listdir(path):
        print(item)

def create_folder(path):
    name = input("Enter folder name: ")
    os.mkdir(os.path.join(path, name))
    print("Folder created successfully!")

def create_file(path):
    name = input("Enter file name (with .txt): ")
    open(os.path.join(path, name), 'w').close()
    print("File created successfully!")

def delete_item(path):
    name = input("Enter file/folder name to delete: ")
    full_path = os.path.join(path, name)

    if os.path.isfile(full_path):
        os.remove(full_path)
        print("File deleted!")
    elif os.path.isdir(full_path):
        shutil.rmtree(full_path)
        print("Folder deleted!")
    else:
        print("File/Folder not found!")

def rename_item(path):
    old = input("Enter old name: ")
    new = input("Enter new name: ")
    os.rename(os.path.join(path, old), os.path.join(path, new))
    print("Renamed successfully!")

def read_file(path):
    name = input("Enter file name to read: ")
    full_path = os.path.join(path, name)

    if os.path.isfile(full_path):
        with open(full_path, 'r') as f:
            print("\nFile Content:\n")
            print(f.read())
    else:
        print("File not found!")

# Main Program
path = os.getcwd()

while True:
    print("\n====== FILE MANAGER ======")
    print("1. Show files")
    print("2. Create folder")
    print("3. Create file")
    print("4. Delete file/folder")
    print("5. Rename file/folder")
    print("6. Read file")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_files(path)
    elif choice == '2':
        create_folder(path)
    elif choice == '3':
        create_file(path)
    elif choice == '4':
        delete_item(path)
    elif choice == '5':
        rename_item(path)
    elif choice == '6':
        read_file(path)
    elif choice == '7':
        print("Exiting File Manager...")
        break
    else:
        print("Invalid choice!")
