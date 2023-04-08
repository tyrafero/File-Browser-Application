import os
import shutil


def copy_folder(src_folder, dest_folder):
    """
    Copy a folder and its contents to a new destination folder.

    :param src_folder: The source folder to copy.
    :type src_folder: str
    :param dest_folder: The destination folder to copy to.
    :type dest_folder: str
    """
    try:
        shutil.copytree(src_folder, dest_folder)
        print(f"Folder {src_folder} copied to {dest_folder}")
    except OSError as e:
        print(f"Error copying folder: {e}")
    
    source_stat = os.stat(src_folder)
    os.chmod(dest_folder, source_stat.st_mode)


