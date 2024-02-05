#!/usr/bin/python3
"""
class mylist
"""


class MyList(list):
    """Inherits from list and provides a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
