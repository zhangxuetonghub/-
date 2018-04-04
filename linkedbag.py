from node import Node
from abstractbag import AbstractBag

class LinkedBag(AbstractBag):
    """包的链表实现"""

    # Constructor
    def __init__(self, sourceCollection=None):
        """
        初始化
        """
        self._items = None
        AbstractBag.__init__(self, sourceCollection)

    # 访问器方法
    def __iter__(self):
        """
        支持迭代，生成器函数（生成器一定是一个迭代器）
        """
        cursor = self._items
        while cursor != None:
            yield cursor.data
            cursor = cursor.next

    # 修改器方法
    def clear(self):
        """
        清空包
        """
        self._size = 0
        self._items = None

    def add(self, item):
        """
        向包里添加新元素
        """
        self._items = Node(item, self._items)
        self._size += 1

    def remove(self, item):
        """
        从包里移除元素
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
