"""
Encrypt and decrypt data using AES encryption.

Author: Arianna Luis
"""

import readwrite
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

BACKEND = default_backend()


def pad(data):
    """
    Pad input data using PKCS7 padding scheme.
    Parameters:
        data (bytes): Data to be padded
    Returns padded data (bytes).
    """
    # PKCS7 padding with 128 bit block size
    padder = padding.PKCS7(128).padder()
    return padder.update(data) + padder.finalize()


def unpad(data):
    """
    Remove padding from decrypted data.
    Parameters:
        data (bytes): Padded data to be unpadded
    Returns unpadded data (bytes).
    """
    # PKCS7 padding with 128 bit block size
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(data) + unpadder.finalize()


def encrypt(filename, aes, key, iv):
    """
    Encrypt the contents of a file using AES encryption.
    Parameters:
        filename (str): Name of the file to encrypt
        aes (str): AES mode for encryption (cbc/ctr)
        key (bytes): Encryption key
        iv (bytes): Initialization vector
    Returns the name of the encrypted file (str).
    """
    # read and pad plaintext
    plaintext = readwrite.read(filename)
    padded_plaintext = pad(plaintext)

    # create Cipher object based on AES mode
    cipher = None
    if aes.lower() == "cbc":
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=BACKEND)
    elif aes.lower() == "ctr":
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=BACKEND)
    else:
        raise ValueError("Invalid AES mode. Valid AES modes are CBC and CTR.")

    # create encryptor object and encrypt padded plaintext
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    # write encrypted text to a new file
    encrypted_filename = filename + ".encrypted"
    readwrite.write(encrypted_filename, ciphertext)

    return encrypted_filename


def decrypt(filename, aes, key, iv):
    """
    Decrypt the contents of an encrypted file using AES
    decryption.
    Parameters:
        filename (str): Name of the file to decrypt
        aes (str): AES mode used for encryption (cbc/ctr)
        key (bytes): Decryption key
        iv (bytes): Initialization vector
    Returns the name of the decrypted file (str).
    """
    # read ciphertext
    ciphertext = readwrite.read(filename)

    # create Cipher object based on the AES mode
    cipher = None
    if aes.lower() == "cbc":
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=BACKEND)
    elif aes.lower() == "ctr":
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=BACKEND)
    else:
        raise ValueError("Invalid AES mode. Valid AES modes are CBC and CTR.")

    # create decryptor object and decrypt ciphertext
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    # try to unpad decrypted data
    try:
        unpadded_data = unpad(decrypted_data)
    # if padding is incorrect, log warning and return data as is
    except ValueError:
        print("Warning: Incorrect padding detected during decryption.")
        unpadded_data = decrypted_data

    # write decrypted data to a new file
    decrypted_filename = filename + ".decrypted"
    readwrite.write(decrypted_filename, unpadded_data)

    return decrypted_filename
