import os


def make_file_exe(path, filename):
    """
    Make the specified file executable.

    :param path: The path of the file to modify.
    :type path: str
    :param filename: The name of the file to modify.
    :type filename: str
    """
    os.chmod(os.path.join(path, filename), 0o755)
