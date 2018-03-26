"""
数据结构（python）开篇程序

"""
import random
def main():
    """
    输入最小数和最大数，计算机从区间随机选择一个数让你猜，猜大告诉你大于，猜小告诉你小于，直到猜中为止，最后告诉你所猜次数
    """
    smaller = int(input("请输入最小数:"))
    larger = int(input("请输入最大数:"))
    MyNumber = random.randint(smaller,larger)
    count = 0
    while True:
        count += 1
        UserNumber = int(input("请输入你要猜的数："))
        if UserNumber > MyNumber:
            print("你猜的数大")
        elif UserNumber < MyNumber:
            print("你猜的数小")
        else:
            break
    
    print("你猜中了，就是{0}，你猜了{1}次".format(MyNumber,count))
    
if __name__ == "__main__":
    main()
