
def read_file(path):
    with open(path, 'rb') as f:
        byte_string=f.read()
        try:
            text = byte_string.decode('utf-8')
        except UnicodeDecodeError:
            text = byte_string.decode('latin-1')
        print(text)

