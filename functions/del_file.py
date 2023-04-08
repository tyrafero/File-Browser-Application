import os


def rm_file(path):
    """
    Remove the file at the specified path.

    :param path: The path of the file to remove.
    :type path: str
    """
    try:
        os.remove(path)
    except OSError as e:
        print(f"You got {e.filename}-{e.strerror} error")
