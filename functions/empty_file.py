import os


def empt_file(path, filename):
    """
    Create an empty file at the specified path with the specified filename.

    :param path: The path of the directory where the file will be created.
    :type path: str
    :param filename: The name of the file to create.
    :type filename: str
    """
    with open(os.path.join(path, filename), 'w') as f:
        pass
