class Counter(object):
    """counter 模块"""
    
    # 类变量
    instances = 0
    
    # 构造函数
    def __init__(self):
        """初始化一个实例"""
        Counter.instances += 1
        self.reset()
        
    # 修改器方法，通过修改对象的实例变量，来修改或改变对象的内部状态
    def reset(self):
        self._value = 0
        
    def increment(self, amount = 1):
        self._value += amount
        
    def decrement(self, amount = 1):
        self._value -= amount
        
    # 访问器方法，直接查看或使用对象的实力变量的值，而不会改变它们
    def getValue(self):
        return self._value
        
    def __str__(self):
        return str(self._value)
        
    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other): return False
        return self._value == other._value
        
if __name__ == '__main__':
    c1 = Counter()
    print(c1)
    print(c1.getValue())
    c1.increment(5)
    print(c1)
    c1.reset()
    print(c1)
    c2 = Counter()
    print(Counter.instances)
    print(c1 == c1)
    print(c1 == 0)
    print(c1 == c2)
    c2.increment()
    print(c1 == c2)
