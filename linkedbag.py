from node import Node


class LinkedBag:
    """Interface for all bag types."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """
        sets the initial state of self, which
        includes the contents of sourceCollection,
        if it's present.
        """
        self.clear()
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """
        Retruns True if len(self) == 0,
        or False otherwise.
        """
        return len(self) == 0

    def __len__(self):
        """
        Returns the number of items in self.
        """
        return self._size

    def __str__(self):
        """
        Retruns the string representation of self.
        """
        return '{' + ','.join(map(str, self)) + '}'

    def __iter__(self):
        """
        Supports iteration over a view of self.
        """
        cursor = self._items
        while cursor != None:
            yield cursor.data
            cursor = cursor.next

    def __add__(self, other):
        """
        Returns a new bag containing the contents
        of self and other.
        """
        result = LinkedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """
        Returns True if self equals other,
        or False otherwise.
        """
        if self is other: return True
        if type(self) != type(other) or \
                len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    # Mutator methods
    def clear(self):
        """
        Makes self becom empty.
        """
        self._size = 0
        self._items = None

    def add(self, item):
        """
        Add item to self.
        """
        self._items = Node(item, self._items)
        self._size += 1

    def remove(self, item):
        """
        Precondition: item is in self.
        Raises: KeyError if item is not in self.
        Postcondition: item is removed from self.
        """
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + ' not in bag')
        # Search for index of target item
        temp = self._items
        if temp.data == item:
            self._items = self._items.next
        else:
            while temp.next.data != item:
                temp = temp.next
            temp.next = temp.next.next
