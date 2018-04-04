class AbstractCollection:
    """Interface for all bag types."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """

        """
        self._size = 0
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

    def __add__(self, other):
        """
        Returns a new bag containing the contents
        of self and other.
        """
        result = type(self)(self)
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

    def clone(self):
        return self
