import os
import shutil

def copy_folder(src_folder, dest_folder):
    try:
        shutil.copytree(src_folder, dest_folder)
        print(f"Folder {src_folder} copied to {dest_folder}")
    except OSError as e:
        print(f"Error copying folder: {e}")
    
    source_stat = os.stat(src_folder)
    os.chmod(dest_folder, source_stat.st_mode)

