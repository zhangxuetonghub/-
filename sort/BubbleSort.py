# 冒泡排序，策略是从列表的开头处开始，比较一对数据项，直到移动到列表的末尾。每当成对的两项之间的顺序不正确的时候，算法就交换它们的位置。这个过程就是将最
# 大的项以冒泡的方式排到了列表的末尾。然后算法从列表开头到倒数第二个列表项，依次类推。最后，列表是已经排序好的。

def bubblesort(lyst):
    j = len(lyst) - 1
    while j > 0:
        m = 0
        while m < j:
            if lyst[m] > lyst[m + 1]:
                lyst[m], lyst[m + 1] = lyst[m + 1], lyst[m]
            m += 1
        j -= 1
        
# def bubblesort(lyst):
#     """改进版本,给定的列表是一个已经排好序的，在一次内循环后就直接返回，不再进行后续操作"""
#     j = len(lyst) - 1
#     while j > 0:
#         swaped = False
#         m = 0
#         while m < j:
#             if lyst[m] > lyst[m+1]:
#                 lyst[m], lyst[m+1] = lyst[m+1], lyst[m]
#                 swaped = True
#             m += 1 
#         if not swaped: return
#         j -= 1


if __name__ == '__main__':
    l = [1,4,2,6,3,9,5]
    bubblesort(l)
    print(l)
