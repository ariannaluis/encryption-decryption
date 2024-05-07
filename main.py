import os
import readwrite
import encrypt_decrypt as ed


def main():
    action = input("Do you want to encrypt or decrypt a file? (e/d) >> ")
    if action.lower() != "e" and action.lower() != "d":
        raise ValueError("Invalid action. Please enter e for encryption or d for decryption.")

    filename = input("Enter the filename >> ")
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")

    aes = input("Enter the AES mode (cbc/ctr) >> ")
    if aes.lower() != "cbc" and aes.lower() != "ctr":
        raise ValueError("Invalid AES mode. Valid AES modes are CBC or CTR.")

    view = ""

    if action.lower() == 'e':
        ed.encrypt(filename, aes)
        view = input("Your file has been encrypted. Would you like to view the contents? (y/n) >> ")
    elif action.lower() == 'd':
        ed.decrypt(filename, aes)
        view = input("Your file has been decrypted. Would you like to view the contents? (y/n) >> ")
    else:
        print("Invalid action")
        return

    if view == "y":
        print(readwrite.read(filename + '.enc'))
    else:
        return


main()
