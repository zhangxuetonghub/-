def indexOfMin(lyst):
    """返回最小值的索引"""
    minIndex = 0
    currentIndex = 1
    l = len(lyst)
    while currentIndex < l:  # 遍历整个列表，算法复杂度为O(n)
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex

if __name__ == '__main__':
    l = [9,3,6,3,3,8,44,1,66,7788]
    print(indexOfMin(l))  
