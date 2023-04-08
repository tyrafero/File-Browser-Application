import os


def ls(directory_path):
    """
    List the contents of the specified directory.
    """
    files = os.listdir(directory_path)
    for file in files:
        print(file)