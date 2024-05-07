from cryptography.hazmat.primitives import padding


def read(filename):
    """reads plaintext from a file and returns it as a string"""
    with open(filename, 'rb') as file:
        return file.read()


def write(filename, text):
    """writes the ciphertext to a file"""
    with open(filename + '.enc', 'wb') as file:
        file.write(text)


def pad(data):
    """pads plaintext to make its length a multiple of the block size
    of the chosen cipher mode"""
    padder = padding.PKCS7(128).padder()
    padded = padder.update(data)
    padded += padder.finalize()
    return padded
