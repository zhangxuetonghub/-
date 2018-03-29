"""
快速排序策略：
1.首先，从列表的中点位置选取一项。这一项叫做基准点。
2.将列表中的项分区，以便小于基准点的所有项都移动到基准点的左边，而剩下的项都移动到基准点的右边。根据相关的实际项，基准点自身的最终位置也是变化的。不管
基准点最终位于何处，这个位置都是它在完全排序的列表中的最终位置。
3.分而治之。对于在基准点分割列表而形成的子列表，递归的重复应用该过程。一个子列表包含了基准点左边的所有的项，另一个子列表包含了基准点右边的所有项。
4.每次遇到少于两个项的一个子列表，就结束这个过程。
"""

"""
分割操作
从程序员的角度来看，该算法最复杂的部分就是对子列表中的项进行分割的操作。
有一种方法较为容易
（1）将基准点和子列表中的最后一项交换
（2）在已知小于基准点的项和剩余的项之间建立一个边界，一开始这个边界就放在第一项之前。
（3）从子列表中的第1项开始，扫描整个子列表。每次遇到小于基准点的项，就将其与边界之后的第一项进行交换，并且边界向后移动。
（4）将基准点和边界之后的第一项交换，从而完成这个过程。
"""
import random

def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation +1, right)
        
def partition(lyst, left, right):
    # 找到基准点，将它换到最后一项
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # 设置分界点为第一个位置
    boundary = left
    # 移动小于基准点的项到左边
    for index in range(left, right):
        if lyst[index] < pivot:
            lyst[index], lyst[boundary] = lyst[boundary], lyst[index]
            boundary += 1
    lyst[right], lyst[boundary] = lyst[boundary], lyst[right]
    return boundary

if __name__ == '__main__':
    l = []
    for i in range(20):
        l.append(random.ranint(1, 21))
    print(l)
    quicksort(l)
    print(l)

# 算法复杂度O(nlog2n)
