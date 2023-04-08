import os


def view_hidden(path):
    """
    List all hidden files in the specified directory.

    :param path: The path of the directory to search.
    :type path: str
    """
    files = [f for f in os.listdir(path) if f.startswith(".")]
    for file in files:
        print(file)
