"""
定义一个数组的实现，使用列表实现（讽刺）
数组更像一个列表，允许客户对数组对象使用下标运算符[]、len函数、str函数和for循环。
"""

class Array(object):
    """定义一个数组类"""
    
    def __init__(self, capacity, fillValue = None):
        """capacity是数组的静态大小， fillValue是数组的填充值"""
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
