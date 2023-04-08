import os

def rm_folder(path):
    try:
        os.rmdir(path)
    except OSError as e:
        print(f"You got {e.filename}-{e.strerror} error")

