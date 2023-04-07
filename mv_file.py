import os

def mv_file(src_path, dest_path):

    os.rename(src_path, dest_path)

mv_file(input("Enter source path: "), input("Enter destination path: "))