import os

directory_location = "/home/tyrafero/Documents/assess1/"


def rn_file(old_file_name, new_file_name):
    """
    Rename a file to a new name.

    :param old_file_name: The old name of the file.
    :type old_file_name: str
    :param new_file_name: The new name for the file.
    :type new_file_name: str
    """
    os.rename(directory_location + old_file_name, directory_location + new_file_name)
