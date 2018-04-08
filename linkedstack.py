from node import Node
from abstractstack import AbstrackStack


class LinkedStack(AbstrackStack):
    """link-base stack implementation"""

    def __init__(self, sourceCollection=None):
        self._items = None
        AbstrackStack.__init__(self, sourceCollection)

    # Accessors
    def __iter__(self):
        def visitNodes(node):
            if not node is None:
                visitNodes(node.next)
                temList.append(node.data)

        temList = list()
        visitNodes(self._items)
        return iter(temList)

    def peek(self):
        if self.isEmpty():
            raise KeyError('The stack is Empty')
        return self._items.data

    # Constructor
    def clear(self):
        self._size = 0
        self._items = None

    def push(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError('The stack is Empty')
        oldItem = self._items.data
        self._items = self._items.next
        self._size -= 1
        return oldItem
