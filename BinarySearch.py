def binarySearch(target, sortedLyst):
    """二叉搜索"""
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

if __name__ == '__main__':
    l = list(range(1000000))
    print(binarySearch(1000,l))

# 可能比顺序搜索更高效，但是有一个额外的整体性代价，必须保持列表是有序的。最坏情况下循环的次数为 n/2/2... 最后商为1的次数 所以算法的复杂度为O(log2N)



            
        
