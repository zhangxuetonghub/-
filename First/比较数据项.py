# 在Python中，内建的Python类型的对象，都可以使用==、<、>这些运算符来进行比较。
# 为了允许算法对一个新的对象的类使用比较运算符== > < ，程序员应该在类中定义__eq__ __lt__和__gt__方法。
# 方法的方法头如下
# def __lt__(self, other): --- "<"
# def __eq__(self, other): --- "==" 
# def __gt__(self, other): --- ">"

class SavingAccount:
    """这是一个储户类，包含开户人的name、pin and balance"""
    def __init__(self, name, pin, balance = 0.0):
        self._name = name
        self._pin = pin
        self._balance = balance
        
    def __eq__(self, other):
        return self._name == other._name
    def __lt__(self, other):
        return self._name < other._name
    def __gt__(self, other):
        return self._name > other._name
    
    
if __name__ == '__main__':
    a = SavingAccount('aaa', 34324)
    b = SavingAccount('abb', 34354)
    c = SavingAccount('aaa', 34364)
    d = SavingAccount('add', 32454)
    print(a < b)
    print(a == c)
print(d > b)
