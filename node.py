class Node(object):
    """定义一个单链表节点类"""
    
    def __init__(self, data, next = None):
        """实例化一个节点使用默认的next为None"""
        self.data = data
        self.next = next
        
# 单链表操作
    
# 遍历    时空线性
probe = head
while probe != None:
    < user or modify probe.data >
    probe = probe.next
        
# 搜索    时空线性
probe = head
while probe != None and targetItem != probe.data:
    probe = probe.next
if probe != None:
    return True
else:
    return False
    
# 访问给定位置  时空线性
probe = head
while index > 0:
    probe = prebo.next
    index -= 1
return probe.data

# 替换 遍历模式 时空线性
（1）替换给定项，同搜索
probe = head
while probe != None and targetItem != probe.data:
    probe = probe.next
if probe != None:
    probe.data = newItem
    return True
else:
    return False
（2）替换给定位置，同访问给定位置
probe = head
while index > 0:
    probe = prebo.next
    index -= 1
probe.data = newItem
    
# 开始处插入 时空常数
head = Node(newItem, head)
    
# 在末尾插入 时空线性
newNode = Node(newItem)
if head is None:
    head = newNode
else:
    probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = newNode
        
# 从开始处删除 时空常数
removeItem = head.data
head = head.next
return removeItem

# 从末尾删除 时空线性
removeItem = head.data
if head.next is None:
    head = None
else:
    probe = head
    while probe.next.next != None:
        probe = probe.next
    removeItem = probe.next.data
    probe.next = None
return removeItem

# 任意位置插入 时空线性
if head is None or index <= 0:
    head = Node(newitem， head)
else:
    probe = head
    while index > 1 and probe.next != None:
        probe = probe.next
        index - = 1
        probe.next = Node(newItem, probe.next)
            
    
# 任意位置删除 时空线性
if index <= 0 or head.next is None:
    removeItem = head.data
    head = head.next
    return removeItem
else:
    probe = head
    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1
    removeItem = probe.next.data
    probe.next = probe.next.next
    return removeItem
    
    
