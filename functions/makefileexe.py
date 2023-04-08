import os

def make_file_exe(path, filename):
    os.chmod(os.path.join(path, filename),0o755)

make_file_exe(input("Enter path to file: "),
              input("Enter file name: "))