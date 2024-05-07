"""
Contains read() and write() functions to read from and write to files
respectively.

Author: Arianna Luis
"""


def read(filename):
    """
    Read from file in binary mode.
    """
    with open(filename, 'rb') as file:
        return file.read()


def write(filename, data):
    """
    Write to file in binary mode.
    """
    with open(filename, 'wb') as file:
        file.write(data)
