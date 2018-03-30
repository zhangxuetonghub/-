class Node(object):
    """定义一个单链表节点类"""
    
    def __init__(self, data, next = None):
        """实例化一个节点使用默认的next为None"""
        self.data = data
        self.next = next
        
if __name__ == '__main__':
    # 创建一个单链表
    head = None
    for count in range(1, 6):
        head = Node(count, head)
    # 遍历一个单链表
    while head != None:
        print(head.data)
        head = head.next
   
    # 将一个列表中的项，转移到一个单链表，保持项的顺序不变       
    l = list(range(1, 10))
    print(l)
    head = None
    for i in l:
        if head == None:
            head = Node(i, None)
        else:
            temp = head
            temp1 = None
            while temp != None:
                temp, temp1 = temp.next, temp
            temp1.next = Node(i, None)
