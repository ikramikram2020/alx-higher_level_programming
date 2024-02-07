#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

