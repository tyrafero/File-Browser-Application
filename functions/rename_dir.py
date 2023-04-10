import os




def rn_folder(old_folder_name, new_folder_name):
    """
    Rename the current working directory to a new name.

    :param new_folder_name: The new name for the folder.
    :type new_folder_name: str
    """
    directory_location = os.getcwd()
    os.rename(directory_location + old_folder_name, directory_location + new_folder_name)
