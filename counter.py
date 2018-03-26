class Counter(object):
    """counter 模块"""
    
    # 类变量
    instances = 0
    
    # 构造函数
    def __init__(self):
        """初始化一个实例"""
        Counter.instances += 1
        self.reset()
        
    # 设置方法
    def reset(self):
        self._value = 0
        
    def increment(self, amount = 1):
        self._value += amount
        
    def decrement(self, amount = 1):
        self._value -= amount
        
    # 访问方法
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
    print(Counter.instences)
    print(c1 == c1)
    print(c1 == 0)
    print(c1 == c2)
    c2.increment()
    print(c1 == c2)
