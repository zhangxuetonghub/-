class Book:
    """图书类"""
    def __init__(self, title, author, onreader = '', waitreaders = []):
        """构造一本书"""
        self._title = title
        self._actor = author
        self._onread = onreader
        self._waitreaders = waitreaders

    def setreader(self, readername):
        """设置正在借阅的读者名字"""
        self._onread = readername

    def getonread(self):
        """获取读者名字"""
        return self._onread
    def getwaitreader(self):
        """获取等待借阅的读者列表"""
        return self._waitreaders

    def addwaitreader(self, reader):
        """添加读者到等待借阅的列表中"""
        self._waitreaders.append(reader)
    
    def __str__(self):
        return 'title:{0} author:{1} ower:{3} waiters:{4}'.format(self._title, self._author, self._onread, self._waitreaders)

    

class Patron:
    """读者类"""
    def __init__(self,name,books = 0, booklist = []):
        """构造读者"""
        self._name = name
        self._books = books
        self._booklist = booklist

    def getname(self):
        return self._name
    def getbooks(self):
        return self._books
    def getbooklist(self):
        return self._booklist

    def borrow(self,book):
        """读者借书的方法"""
        if book.getonread() == self._name:
            print("你已经借了这本书，还没有归还！")
        elif self._books == 3:
            print("你已经借阅了3本书，请归还其他书再来借阅！")
        elif book.getonread() != '':
            if self not in book.getwaitreader():
                book.addwaitreader(self)
                print("这本书已经借出去了，已经为你排队")
            else:
                print("这本书已经借出去了，你已经在队列中")
        elif  book.getwaitreader() == []:
            self._books += 1
            self._booklist.append(book)
            book.setreader(self._name)
        else:
            if book.getwaitreader()[0] is self:
                self._books += 1
                self._booklist.append(book)
                book.setreader(self._name)
                book._waitreaders.pop(0)
            else:
                if self in book.getwaitreader():
                    print("还没有到你的排队位置")
                else:
                    book.addwaitreader(self)
                    print("已经为你排队")

    def sendback(self, book):
        """读者还书的方法"""
        if book.getonread() != self._name or self._books == 0:
            print("这本书没有在你的手中或者你的手中没有图书，无法归还！")
        else:
            self._books -= 1
            self._booklist.remove(book)
            book.setreader('')
    
    def __str__(self):
        return 'name:{0} books:{1} booklist:{2}'.format(self._name, self._books, self._booklist)
     
# class Library:
#     """图书馆类"""
#     def __init__(self,booklist = [], patronlist = []):
#         """构造函数"""
#         self._booklist = booklist
#         self._patronlist = patronlist
        
#     def addbook(self, book):
#         """添加图书"""
#         if book in self._booklist:
#             print('此书已经添加，不需要重复添加')
#         else:
#             self._booklist.append(book)
    
#     def addpatron(self, patron):
#         """添加读者"""
#         if patron in self._patronlist:
#             print('此读者已经添加，不需要重复添加')
#         else:
#             self._patronlist.append(patron)
     
    
        
    
    

if __name__ == '__main__':
    b1 = Book('yuwen','zxt')
    b2 = Book('shuxue','zxt')
    b3 = Book('wuli','zxt')
    b4 = Book('shengwu','zxt')
    p1 = Patron('zhangxutong')
    p2 = Patron('kongxiaojuan')
    p3 = Patron('zhangjiani')
    p1.borrow(b1)
    p1.borrow(b2)
    p1.borrow(b3)
    p2.borrow(b1)
    p3.borrow(b1)
    p1.sendback(b1)
    p2.borrow(b1)
    p3.borrow(b1)
    p2.sendback(b1)
    p1.borrow(b1)
    p3.borrow(b1)
    p3.sendback(b1)
    p1.borrow(b1)
    p1.borrow(b4)

    print(p1,b1)
