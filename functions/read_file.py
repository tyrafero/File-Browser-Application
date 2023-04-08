def read_file(path):
    """
    Read a file from the specified path and print its contents to the console.

    :param path: The path of the file to read.
    :type path: str
    """
    with open(path, 'rb') as f:
        byte_string = f.read()
        try:
            text = byte_string.decode('utf-8')
        except UnicodeDecodeError:
            text = byte_string.decode('latin-1')
        print(text)
