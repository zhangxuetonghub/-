from abstractcollection import AbstractCollection


class AbstractBag(AbstractCollection):
    """Interface for all bag types."""

    # Constructor
    def __init__(self, sourceCollection=None):

        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """
        Retruns the string representation of self.
        """
        return '{' + ','.join(map(str, self)) + '}'

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
