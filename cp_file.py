import os
from list_all_dir import ls

directory_location = "/home/tyrafero/Documents/assess1/"

def cp_file():
    """
    Copy a file from a source path to a destination path.
    """
    # Prompt user to enter source and destination paths
    src_path = input("Enter the path to the source file: ")
    dest_path = input("Enter the path to the destination file: ")

    # Copy the source file to the destination path
    with open(src_path, 'rb') as src_file:
        with open(dest_path, 'wb') as dest_file:
            dest_file.write(src_file.read())

    # Copy the source file's permissions to the destination file
    source_stat = os.stat(src_path)
    os.chmod(dest_path, source_stat.st_mode)

# Call the cp() function
cp_file()

# List the contents of the directory
ls(directory_location)
