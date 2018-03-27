class Book:
    """图书类"""

    def __init__(self, title, author):
        """构造一本书"""
        self._title = title
        self._author = author
        self._onread = ''
        self._waitreaders = []

    def setreader(self, readername):
        """设置正在借阅的读者名字"""
        self._onread = readername

    def gettitle(self):
        return self._title

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
        return '图书名:{0} 作者:{1} 读者:{2} 等待借阅的读者列表:{3}'.format(self._title, self._author,'无' if self._onread == '' else self._onread,self._waitreaders)

    def __repr__(self):
        return self._title



class Patron:
    """读者类"""

    def __init__(self, name):
        """构造读者"""
        self._name = name
        self._books = 0
        self._booklist = []

    def getname(self):
        return self._name

    def getbooks(self):
        return self._books

    def getbooklist(self):
        return self._booklist

    def borrow(self, book):
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
        elif book.getwaitreader() == []:
            self._books += 1
            self._booklist.append(book)
            book.setreader(self._name)
            print(self.getname(), "借阅了", book.gettitle())
        else:
            if book.getwaitreader()[0] is self:
                self._books += 1
                self._booklist.append(book)
                book.setreader(self._name)
                book._waitreaders.pop(0)
                print(self.getname(),"借阅了",book.gettitle())
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
            print(self.getname(), "归还了", book.gettitle())

    def __str__(self):
        return '姓名:{0} 借书数量:{1} 所借图书:{2}'.format(self._name, self._books, self._booklist)

    def __repr__(self):
        return self._name


class Library:
    """图书馆类"""
    def __init__(self):
        """构造函数"""
        self._booklist = []
        self._patronlist = []

    def addbook(self, book):
        """添加图书"""
        if book in self._booklist:
            print('此书已经添加，不需要重复添加')
        else:
            self._booklist.append(book)

    def addpatron(self, patron):
        """添加读者"""
        if patron in self._patronlist:
            print('此读者已经添加，不需要重复添加')
        else:
            self._patronlist.append(patron)


    def deletebook(self, book):
        """删除图书"""
        if book in self._booklist:
            self._booklist.remove(book)
            print("成功删除{0}".format(book.gettitle()))
        else:
            print("没有这本书，无法删除！")

    def deletepatron(self, patron):
        """删除读者"""
        if patron in self._patronlist:
            self._patronlist.remove(patron)
            print("成功删除{0}".format(patron.getname()))
        else:
            print("没有这个读者，无法删除！")

    def searchbooktitle(self,booktitle):
        """通过书标题搜索图书"""
        if booktitle in [x.gettitle() for x in self._booklist]:
            for i in self._booklist:
                if i.gettitle() == booktitle:
                    print(i)
        else:
            print("没有这本书")

    def searchpatronname(self,patronname):
        """通过读者名字搜索读者"""
        if patronname in [x.getname() for x in self._patronlist]:
            for i in self._patronlist:
                if i.getname() == patronname:
                    print(i)
        else:
            print("没有这位读者")



if __name__ == '__main__':
    b1 = Book('语文', 'zxt')
    b2 = Book('数学', 'zxt')
    b3 = Book('物理', 'zxt')
    b4 = Book('化学', 'zxt')
    p1 = Patron('张无忌')
    p2 = Patron('孙行者')
    p3 = Patron('钟无艳')
    l = Library()
    l.addbook(b1)
    l.addbook(b2)
    l.addbook(b3)
    l.addbook(b4)
    l.addpatron(p1)
    l.addpatron(p2)
    l.addpatron(p3)
    p1.borrow(b1)
    p1.borrow(b2)
    p1.borrow(b3)
    p2.borrow(b1)
    p3.borrow(b1)
    l.searchbooktitle('语文')
    l.searchpatronname('张无忌')
    p1.sendback(b1)
    p2.borrow(b1)
    p3.borrow(b1)
    p2.sendback(b1)
    p1.borrow(b1)
    p3.borrow(b1)
    p3.sendback(b1)
    p1.borrow(b1)
    p1.borrow(b4)
    l.searchbooktitle('语文')

