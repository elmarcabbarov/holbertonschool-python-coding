#!/usr/bin/python3
"""Module that defines a Square class with size getter/setter"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize square"""
        self.size = size   # IMPORTANT: use setter for validation

    @property
    def size(self):
        """Get current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area"""
        return self.__size * self.__size
