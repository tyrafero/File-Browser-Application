import os

def hide_file(path,filename):

    filepath= os.path.join(path,filename)
    os.rename(filepath,
              os.path.join(path,"."+filename))
    
hide_file(input("Enter path to file: "),
          input("Enter file name: "))