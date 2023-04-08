import os


def mv_dir(src_path, dest_path):
    """
    Move or rename a directory from a source path to a destination path.

    :param src_path: The path of the directory to move or rename.
    :type src_path: str
    :param dest_path: The new path for the directory.
    :type dest_path: str
    """
    os.rename(src_path, dest_path)