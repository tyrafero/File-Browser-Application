import string
import random


def rand_text(path,filename):
    with open(path + filename, 'w') as f:
        # Generate 10 lines of 20 random characters each
        for i in range(5):
            line = ''.join(random.choice(string.ascii_lowercase) for _ in range(20))
            f.write(line + '\n')


