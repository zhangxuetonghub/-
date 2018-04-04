from abstractcollection import AbstractCollection


class AbstractBag(AbstractCollection):
    """Interface for all bag types."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """初始化"""
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """
        返回包的字符串表示 -->str
        """
        return '{' + ','.join(map(str, self)) + '}'

    def __eq__(self, other):
        """
        比较两个包是否相等 重载“==” -->bool
        """
        if self is other: return True
        if type(self) != type(other) or \
                len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True
