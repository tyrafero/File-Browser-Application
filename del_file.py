import os

def rm_file(path):
    try:
        os.remove(path)
    except OSError as e:
        print(f"You got {e.filename}-{e.strerror} error")

rm_file(input("Enter the file path: "))