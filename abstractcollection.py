class AbstractCollection:
    """Interface for all bag types."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """
        初始化
        """
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """
        判断集合是否为空 -->bool
        """
        return len(self) == 0

    def __len__(self):
        """
        返回集合长度 -->int
        """
        return self._size

    def __str__(self):
        """
        返回集合的字符串表示 -->str
        """
        return '[' + ']['.join(map(str, self)) + ']'

    def __add__(self, other):
        """
        返回一个合并后的集合 -->type(self)
        """
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """
        判断两个集合是否相等 重载运算符“==”
        """
        if self is other: return True
        if type(self) != type(other) or \
                len(self) != len(other):
            return False
        
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True
    
#         for item in self:
#             if not item in other:
#                 return False
#         return True
         
    
