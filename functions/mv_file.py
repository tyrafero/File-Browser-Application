import os


def mv_file(src_path, dest_path):
    """
    Move or rename a file from a source path to a destination path.

    :param src_path: The path of the file to move or rename.
    :type src_path: str
    :param dest_path: The new path for the file.
    :type dest_path: str
    """
    os.rename(src_path, dest_path)
