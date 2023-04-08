import os


def hide_file(path, filename):
    """
    Rename a file to make it hidden.

    :param path: The path of the file.
    :type path: str
    :param filename: The name of the file to hide.
    :type filename: str
    """
    filepath = os.path.join(path, filename)
    os.rename(filepath, os.path.join(path, "." + filename))
