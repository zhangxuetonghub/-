def swap(lyst, i, j):
    """交换列表中的两项的位置"""
    lyst[i], lyst[j] = lyst[j], lyst[i]
#     temp = lyst[i]
#     lyst[i] = lyst[j]
#     lyst[j] = temp

# 为其他排序算法提供服务

if __name__ == '__main__':
    l = [1,2,3,4,5]
    swap(l, 0, 4)
    print(l)
