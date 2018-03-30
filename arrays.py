"""
定义一个数组的实现，使用列表实现（讽刺）
数组更像一个列表，允许客户对数组对象使用下标运算符[]、len函数、str函数和for循环。
数组是列表的一个非常受限制的版本
"""

class Array(object):
    """定义一个数组类"""
    
    def __init__(self, capacity, fillValue = None):
        """capacity大小， fillValue是填充值"""
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)
            
    def __len__(self):
        """-> 数组大小"""
        return len(self._items)
    
    def __str__(self):
        """-> 数组的字符串形式"""
        return str(self._items)
    
    def __iter__(self):
        """支持迭代，返回一个迭代器"""
        return iter(self._items)
    
    def __getitem__(self, index):
        """下标操作->索引访问"""
        return self._items[index]
    
    def __setitem__(self, index, newItem):
        """下标操作->替换"""
        self._items[index] = newItem
        
        
if __name__ == '__main__':
    a = Array(10)
    print(len(a))
    print(a)
    for i in a:
        print(i)
    a[9] = 10
    print(a[9])

"""
数组操作
1.增加数组的大小（×2）
2.减少数组的大小（if size <= 1/4 -> 1/2）
3.在数组中插入一项（索引位置后的每一项 --> 向后移动一个位置，新元素放到当前索引位置，有可能会触发1操作）
4.从数组中删除一项（索引后的每一项 <-- 向前移动一个位置，有可能会触发2操作)
"""
