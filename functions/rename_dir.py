import os
directory_location = "/home/tyrafero/Documents/assess1/"

def rn_folder(old_folder_name,new_folder_name):
    """
    Rename the current working directory to a new name.

    :param new_folder_name: The new name for the folder.
    :type new_folder_name: str
    """
    os.rename(directory_location+old_folder_name, directory_location+new_folder_name)

