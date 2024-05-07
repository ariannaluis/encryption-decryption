"""
Read from and write to files.

Author: Arianna Luis
"""


def read(filename):
    """
    Read contents of a file.
    Parameters:
        filename (str): Name of the file to read from
    Returns contents of the file (bytes).
    """
    with open(filename, 'rb') as file:
        return file.read()


def write(filename, data):
    """
    Write data to a file.
    Parameters:
        filename (str): Name of the file to write to
        data (bytes): Data to write to the file
    """
    with open(filename, 'wb') as file:
        file.write(data)
