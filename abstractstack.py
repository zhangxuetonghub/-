"""
file: abstrackstack.py
"""

from abstractcollection import AbstractCollection

class AbstrackStack(AbstractCollection):
    """An abstrack stack implementation"""

    # Constructor
    def __init__(self, sourceCollection = None):
        AbstractCollection.__init__(self, sourceCollection)

    def add(self, item):
        """ Adds item to self"""
        self.push(item)
