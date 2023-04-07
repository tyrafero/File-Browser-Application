import os
directory_location= "/home/tyrafero/Documents/assess1/"

def ls(directory_path):
    """
    List the contents of the specified directory.

    """
    files = os.listdir(directory_path)
    for file in files:
        print(file)


ls(directory_location)