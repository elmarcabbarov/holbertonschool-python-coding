#!/usr/bin/python3
"""Module that defines a Square class"""
class Square:
    """A class that defines a square by its size"""
    def __init__(self, size):
        """Initialize a square with a given size
        Args:
            size: The size of the square (no type/value verification)
        """
        self.__size = size
