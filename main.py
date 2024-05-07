"""
Command-line interface for encrypting and decrypting files
using AES encryption.

Author: Arianna Luis
"""

import os
import keys
import readwrite
import encrypt_decrypt as ed


def main():
    # get action to be performed, filename, and aes mode
    action = input("Do you want to encrypt or decrypt a file? (e/d) >> ")
    filename = input("Enter the filename >> ")
    aes = input("Enter the AES mode (cbc/ctr) >> ")

    # error handling for invalid filename
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")

    # handle encryption
    if action == 'e':
        # generate key and iv, save to .key file
        key = keys.generate_key()
        iv = keys.generate_iv()
        key_filename = keys.save_key_and_iv(key, iv, filename)

        # encrypt file
        encrypted_file = ed.encrypt(filename, aes, key, iv)

        # completion message and view option
        print(f"The content of '{filename}' has been encrypted and saved to '{encrypted_file}'.")
        print(f"The encryption key and IV have been saved to '{key_filename}'.")
        view = input("Would you like to view the encrypted content? (y/n) >> ")

        # print content if user wants to view
        if view.lower() == "y":
            print("Encrypted content:")
            print(readwrite.read(encrypted_file))

    # handle decryption
    elif action == 'd':
        # get key and iv
        key_filename = input("Enter the filename containing the decryption key and IV >> ")
        with open(key_filename, 'rb') as key_file:
            key = key_file.read(32)
            iv = key_file.read(16)

        # decrypt file
        decrypted_file = ed.decrypt(filename, aes, key, iv)

        # completion message and view option
        print(f"The content of '{filename}' has been decrypted and saved to '{decrypted_file}'.")
        view = input("Would you like to view the decrypted content? (y/n) >> ")

        # print content if user wants to view
        if view.lower() == "y":
            decrypted_content = readwrite.read(decrypted_file).decode("utf-8")
            print("Decrypted content:")
            print(decrypted_content)
    else:
        print("Invalid action. Please enter 'e' for encryption or 'd' for decryption.")


main()
