import os
def empt_file(path,filename):
    with open(os.path.join(path,filename), 'w') as f:
        pass

