class Node(object):
    """定义一个单链表节点类"""
    
    def __init__(self, data, next = None):
        """实例化一个节点使用默认的next为None"""
        self.data = data
        self.next = next
        
if __name__ == '__main__':
    head = None
    for count in range(1, 6):
        head = Node(count, head)
        
    print(head.data)
        
