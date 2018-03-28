def sequentialSearch(target, lyst):
    """如果找到目标项，返回它的索引；否则返回-1"""
    position = 0
    while position < len(lyst):
        if lyst[position] == target:
            return position
        position += 1
    return -1

if __name__ == '__main__':
    l = [1,2,3,4,5,6]
    print(sequentialSearch(5,l))
    print(sequentialSearch(8,l))

# 模拟 in 操作
# 最好情况 第一项就找到       O(1) 
# 最坏情况最后一项才找到      O(n) 
# 平均情况（（n+1)/2         O(n)
