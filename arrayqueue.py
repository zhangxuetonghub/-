from abstractcollection import AbstractCollection
from arrays import Array

class ArrayQueue(AbstractCollection):
    DEFAULT_SIZE = 10

    def __init__(self, sourceCollection = None):
        self._front = 0
        self._rear = 0
        self._items = Array(ArrayQueue.DEFAULT_SIZE)
        AbstractCollection.__init__(self, sourceCollection)

    def __iter__(self):
        if self._rear > self._front or self._rear == self._front and self._size == 0:
            i = self._front
            while i < self._rear:
                yield self._items[i]
                i += 1
        else:
            i = self._front
            while i < len(self._items):
                yield self._items[i]
                i += 1
            i = 0
            while i < self._rear:
                yield self._items[i]
                i += 1

    def qlen(self):
        return len(self._items)

    def add(self, newItem):
        """Adds newItem to the rear of the queue."""
        if self._size == len(self._items):
            temp = Array(self._size * 2)
            if self._rear == 0:
                i = 0
                while i < len(self._items):
                    temp[i] = self._items[i]
                    i += 1
                self._items = temp
            else:
                i = 0
                j = self._front
                while j < len(self._items):
                    temp[i] = self._items[j]
                    i += 1
                    j += 1
                j = 0
                while j < self._rear:
                    temp[i] = self._items[j]
                    i += 1
                    j += 1
                self._items = temp
            self._front = 0
            self._rear = self._size

        self._items[self._rear] = newItem
        self._rear += 1
#         if self._rear == len(self._items):
#             self._rear = 0
        self._rear = self._rear % len(self._items)
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError('The Queue is Empty')
        oldItem = self._items[self._front]
        self._front += 1
#         if self._front == len(self._items):
#             self._front = 0
        self._front = self._front % len(self._items)
        self._size -= 1

        if self._size < len(self._items) // 4 and \
                len(self._items) >= ArrayQueue.DEFAULT_SIZE * 2:
            temp = Array(len(self._items) // 2)
            if self._rear > self._front:
                i = 0
                j = self._front
                while i < self._rear:
                    temp[i] = self._items[j]
                    i += 1
                    j += 1
                self._items = temp
            else:
                i = 0
                j = self._front
                while j < len(self._items):
                    temp[i] = self._items[j]
                    i += 1
                    j += 1
                j = 0
                while j < self._rear:
                    temp[i] = self._items[j]
                    i += 1
                    j += 1
                self._items = temp
            self._front = 0
            self._rear = self._size

        return oldItem

    def peek(self):
        if self.isEmpty():
            raise KeyError('The Queue is Empty')
        return self._items[self._front]
