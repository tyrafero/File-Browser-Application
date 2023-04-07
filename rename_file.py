import os
directory_location = "/home/tyrafero/Documents/assess1/"

def rn_file(old_file_name,new_file_name):

    os.rename(directory_location+old_file_name, directory_location+new_file_name)

rn_file(input("Old file name: "), input("New file name: "))