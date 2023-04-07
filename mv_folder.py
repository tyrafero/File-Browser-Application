import os

def mv_dir(src_path, dest_path):

    os.rename(src_path, dest_path)

mv_dir(input("Enter source path: "), input("Enter destination path: "))