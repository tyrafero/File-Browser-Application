import os
directory_location= input("Enter location of directory")

def rn_folder(new_folder_name):
    """
    Rename the current working directory to a new name.

    :param new_folder_name: The new name for the folder.
    :type new_folder_name: str
    """
    new_folder_path = os.path.join(os.path.dirname(directory_location), new_folder_name)
    os.rename(directory_location, new_folder_path)

rn_folder(input("Enter a new folder name: "))