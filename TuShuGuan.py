class Book:
    def __init__(self, title, author, onreader = '', waitreaders = []):
        self._title = title
        self._actor = author
        self._onread = onreader
        self._waitreaders = waitreaders

    def setreader(self, readername):
        self._onread = readername

    def getonread(self):
        return self._onread

    def addwaitreader(self, reader):
        self._waitreaders.append(reader)

    def getwaitreader(self):
        return self._waitreaders

class Patron:

    def __init__(self,name,books = 0):
        self._name = name
        self._books = books

    def getname(self):
        return self._name

    def getbooks(self):
        return self._books

    def borrow(self,book):
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
            book.setreader(self._name)
        else:
            if book.getwaitreader()[0] is self:
                self._books += 1
                book.setreader(self._name)
                book._waitreaders.pop(0)
            else:
                if self in book.getwaitreader():
                    print("还没有到你的排队位置")
                else:
                    book.addwaitreader(self)
                    print("已经为你排队")

    def sendback(self, book):
        if book.getonread() != self._name or self._books == 0:
            print("这本书没有在你的手中或者你的手中没有图书，无法归还！")
        else:
            self._books -= 1
            book.setreader('')

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

    print(p1.getbooks(),b1.getwaitreader())
