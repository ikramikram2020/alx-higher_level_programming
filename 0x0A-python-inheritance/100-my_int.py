#!/usr/bin/python3
"""
Module containing the MyInt class
"""


class MyInt(int):
    """
    MyInt class,
    inherits from int
    """

    def __eq__(self, other):
        """
        Override equality operator
        true
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override inequality operator
        false
        """
        return super().__eq__(other)
