import os


def rm_folder(path):
    """
    Remove the folder at the specified path.

    :param path: The path of the folder to remove.
    :type path: str
    """
    try:
        os.rmdir(path)
    except OSError as e:
        print(f"You got {e.filename}-{e.strerror} error")
