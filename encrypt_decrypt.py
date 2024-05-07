import readwrite
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


KEY = os.urandom(32)
IV = os.urandom(16)
BACKEND = default_backend()


def encrypt(filename, aes):
    plaintext = readwrite.read(filename)
    padded_plaintext = readwrite.pad(plaintext)

    cipher = None
    if aes.lower() == "cbc":
        cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=BACKEND)
    elif aes.lower() == "ctr":
        cipher = Cipher(algorithms.AES(KEY), modes.CTR(IV), backend=BACKEND)
    else:
        raise Exception("Invalid AES mode. Valid AES modes are CBC and CTR.")

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    readwrite.write(filename, ciphertext)


def decrypt(filename, aes):
    # read file
    ciphertext = readwrite.read(filename)

    # get aes mode
    if aes.lower() == "cbc":
        cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV))
    elif aes.lower() == "ctr":
        cipher = Cipher(algorithms.AES(KEY), modes.CTR(IV))
    else:
        return

    # decrypt file using aes mode
    dec = cipher.decryptor()
    plaintext = dec.update(ciphertext) + dec.finalize()

    # write decrypted text to output file
    readwrite.write(filename, plaintext)