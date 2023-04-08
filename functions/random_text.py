import string
import random


def rand_text(path, filename):
    """
    Create a file with random text at the specified path with the specified filename.

    :param path: The path of the directory where the file will be created.
    :type path: str
    :param filename: The name of the file to create.
    :type filename: str
    """
    with open(path + filename, 'w') as f:
        # Generate 5 lines of 20 random lowercase characters each
        for i in range(5):
            line = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
            f.write(line + '\n')
