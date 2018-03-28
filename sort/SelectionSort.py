def swap(lyst, i, j):
    """交换列表中的两项的位置"""
    lyst[i], lyst[j] = lyst[j], lyst[i]

def selectionSort(lyst):
    """选择排序"""
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1
        
# 排序思路 (>_<)
# 从第一项开始顺序搜索整个表，选择整个表中最小的一项和第一项交换位置（最小的项放到了第一个位置）
# 然后从第二项开始搜索后续表，选择后续表中最小的一项和第二项交换位置（第二小的项放到了第二个位置）
# ... ... 依次类推直到最后一项，排序完成。
        
        
if __name__ == '__main__':
    l = [1,8,2,3,7,4,5]
    selectionSort(l)
    print(l)
