"""
file:arraystack.py
"""

from arrays import Array
from abstractstack import AbstrackStack

class ArrayStack(AbstrackStack):
    """ An array-base stack implementation"""
    DEFAULT_SIZE = 10

    def __init__(self, sourceCollection = None):
        """init"""
        self._items = Array(ArrayStack.DEFAULT_SIZE)
        AbstrackStack.__init__(self, sourceCollection)

    # Accessors
    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        if self.isEmpty():
            raise KeyError('stack is Empty')
        return self._items[len(self) - 1]

    # Mutators
    def clear(self):
        self._size = 0
        self._items =Array(ArrayStack.DEFAULT_SIZE)

    def push(self, item):
        """"""
        if self._size == len(self._items):
            temp = Array(self._size * 2)
            for i in range(self._size):
                temp[i] = self._items[i]
            self._items = temp

        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError('stack is Empty')
        oldItem = self._items[len(self) - 1]
        self._size -= 1
        #
        if self._size < len(self._items) // 4 and \
                len(self._items) >= ArrayStack.DEFAULT_SIZE * 2:
            temp = Array(len(self._items) // 2)
            for i in range(self._size):
                temp[i] = self._items[i]
            self._items = temp
        return oldItem
