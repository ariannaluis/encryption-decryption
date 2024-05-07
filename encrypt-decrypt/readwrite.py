def read(filename):
    """reads plaintext from a file and returns it as a string"""
    with open(filename, 'r') as file:
        return file.read()


def write(filename, text):
    """writes the ciphertext to a file"""
    with open(filename, 'w') as file:
        file.write(text)
