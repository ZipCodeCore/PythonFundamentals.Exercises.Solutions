from typing import TypeVar

N = TypeVar('N', int, float)


class Rectangle:
    def __init__(self, length: N, width: N):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length: N):
        super().__init__(length, length)
