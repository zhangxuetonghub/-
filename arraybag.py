from arrays import Array

class ArrayBag:
    """包的数组实现类"""

    DEFALUT_SIZE = 10

    # Constructor
    def __init__(self, sourceCollection=None):
        """
        初始化
        """
        self.clear()
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """
        查看包是否为空
        """
        return len(self) == 0

    def __len__(self):
        """
        返回包的长度
        """
        return self._size

    def __str__(self):
        """
        返回包字符串表示
        """
        return '{' + ','.join(map(str, self)) + '}'

    def __iter__(self):
        """
        支持迭代，返回生成器（生成器一定是一个迭代器）
        """
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __add__(self, other):
        """
        运算符“+”重载
        """
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """
        运算符“==”重载
        """
        if self is other:return True
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
        清空包
        """
        self._size = 0
        self._items = Array(ArrayBag.DEFALUT_SIZE)

    def add(self, item):
        """
        向包里添加新元素
        """
        if self._size == len(self._items):
            temp = Array(self._size * 2)
            for i in range(self._size):
                temp[i] = self._items[i]
            self._items = temp
        self._items[len(self)] = item
        self._size += 1

    def remove(self, item):
        """
        从包里移除元素
        Precondition: item is in self.
        Raises: KeyError if item is not in self.
        Postcondition: item is removed from self.
        """
        # 检查要移除的元素是否在包里，如果没有，抛出异常
        if not item in self:
            raise KeyError(str(item) + 'not in bag')
        # 搜索要删除的元素的位置
        targetindex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetindex += 1
        # 待移除元素的后的所有元素都向前移一个位置
        for i in range(targetindex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        self._size -= 1
        # 判断是否浪费了大量的内存，如果有，数组减半
        if self._size < len(self._items) // 4 and \
                len(self._items) >= ArrayBag.DEFALUT_SIZE * 2:
            temp = Array(len(self._items) // 2)
            for i in range(self._size):
                temp[i] = self._items[i]
            self._items = temp

            
class ArraySortedBag(ArrayBag):
    """
    通过继承创建一个数组实现的有序包类
    """

    # Constructor
    def __init__(self, sourceCollection=None):
        ArrayBag.__init__(self, sourceCollection)
    
    # 增加方法 “in”操作
    def __contains__(self, item):
        """return True if item is in self, or Return False"""
        left = 0
        right = len(self) - 1
        while left <= right:
            midPoint = (left + right) // 2
            if self._items[midPoint] == item:
                return True
            elif self._items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        return False

    # 改写add方法，
    def add(self, item):
        if self._size == len(self._items):
            temp = Array(self._size * 2)
            for i in range(self._size):
                temp[i] = self._items[i]
            self._items = temp

        #
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            ArrayBag.add(self, item)
        else:
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i - 1]
            self._items[targetIndex] = item
            self._size += 1
