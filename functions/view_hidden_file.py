import os

def view_hidden(path):
    files=[f for f in os.listdir(path) 
           if f.startswith(".")]
    for file in files:
        print(file)

view_hidden(input("Enter the path of the directory: "))