from functions import cp_file, cp_folder
from functions import del_file, del_folder
from functions import hide_file, view_hidden_file
from functions import rename_file, rename_dir
from functions import mv_file, mv_folder
from functions import list_all_dir, read_file
from functions import empty_file, makefileexe, random_text

def main():
    while True:
        print("Available options:")
        print("1. Copy file")
        print("2. Copy folder")
        print("3. Delete file")
        print("4. Delete folder")
        print("5. Hide file")
        print("6. Show hidden files")
        print("7. Rename file")
        print("8. Rename folder")
        print("9. Move file")
        print("10. Move folder")
        print("11. Create empty file")
        print("12. Make file executable")
        print("13. List directory contents")
        print("14. Read file content")
        print("15. Create random text file")
        print("q . Quit")

        choice = input("Enter your choice: ")

        if choice == "q":
            break
        elif choice == "1":
            cp_file.cp_file(input("Enter the path to the source file: "), 
                            input("Enter the path to the destination file: "))
        elif choice == "2":
            cp_folder.copy_folder(input("Enter Folder path  to copy: "), 
                                   input("Enter Destination Folder with name: "))
        elif choice == "3":
            del_file.rm_file(input("Enter the file path: "))
        elif choice == "4":
            del_folder.rm_folder(input("Enter the folder path: "))
        elif choice == "5":
            hide_file.hide_file(input("Enter path to file: "), 
                                input("Enter file name: "))
        elif choice == "6":
            view_hidden_file.view_hidden(input("Enter the directory path: "))
        elif choice == "7":
            rename_file.rn_file(input("Old file name: "), 
                                input("New file name: "))
        elif choice == "8":
            rename_dir.rn_dir(input("Old dir name: "), 
                              input("New dir name: "))
        elif choice == "9":
            mv_file.mv_file(input("Enter source path: "), 
                            input("Enter destination path: "))
        elif choice == "10":
            mv_folder.mv_dir(input("Enter source path: "), 
                             input("Enter destination path: "))
        elif choice == "11":
            empty_file.empt_file(input("Enter path for file: "), 
                                 input("Enter desired file name: "))
        elif choice == "12":
            makefileexe.make_file_exe(input("Enter path to file: "), 
                                      input("Enter file name: "))
        elif choice == "13":
            list_all_dir.ls(input("Enter the directory path: "))
        elif choice == "14":
            read_file.read_file(input("Enter path of file to read: "))
        elif choice == "15":
            random_text.rand_text(input("Enter path for file: "), 
                                  input("Enter filename: "))
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
