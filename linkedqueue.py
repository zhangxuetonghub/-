from abstractcollection import AbstractCollection
from node import Node

class LinkedQueue(AbstractCollection):

    def __init__(self, sourceCollection = None):
        self._front = None
        self._rear = None
        AbstractCollection.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = self._front
        while cursor != None:
            yield cursor.data
            cursor = cursor.next

    def add(self, newItem):
        """Adds newItem to the rear of the queue."""
        newNode = Node(newItem, None)
        if self.isEmpty():
            self._front = newNode
            self._rear = newNode
            self._size += 1
        else:
            self._rear.next = newNode
            self._rear = newNode
            self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError('The Queue is Empty')
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem

    def peek(self):
        if self.isEmpty():
            raise KeyError('The Queue is Empty')
        return self._front.data
