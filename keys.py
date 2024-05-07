"""
Generate and save encryption keys and initialization vectors.
"""

import os


def generate_key():
    """
    Generate a random encryption key.
    Returns the generated encryption key (bytes).
    """
    # AES-256: key length is 32 bytes
    return os.urandom(32)


def generate_iv():
    """
    Generate a random initialization vector.
    Returns the generated initialization vector (bytes).
    """
    # IV length = block size (AES = 16 bytes)
    return os.urandom(16)


def save_key_and_iv(key, iv, filename):
    """
    Save the encryption key and initialization vector to a new file.
    Parameters:
        key (bytes): Encryption key
        iv (bytes): Initialization vector
        filename (str): filename related to the key and IV
    """
    # generate new filename
    key_filename = filename + ".key"

    # write key and IV to new file
    with open(key_filename, 'wb') as key_file:
        key_file.write(key)
        key_file.write(iv)

    return key_filename
