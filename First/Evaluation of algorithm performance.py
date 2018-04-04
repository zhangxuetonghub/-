# 1.度量算法的运行时间
import time
ProblemSize = 10000000
print('{0:<13}{1:<16}'.format('ProbleSize', 'Seconds'))
for count in range(5):
    
    start = time.clock()
    # 算法开始
    work = 1
    for x in range(ProblemSize):
        work += 1
        work -= 1
    # 算法结束
    elapsed = time.clock() - start
    
    print('{0:<13}{1:<16.3}'.format(ProblemSize, elapsed))
    ProblemSize *= 2
"""
结果
ProbleSize   Seconds         
10000000     1.07            
20000000     2.16            
40000000     4.24            
80000000     8.43            
160000000    16.9
"""
# 问题：不同硬件平台的处理速度不同，不同的编程语言和编译器也会得到性能不同的代码。对于很大的数据集合来说，确定某些算法的运行时间是不切实际的。
---------------------------------------------------------------------------------------------------------------------------------
# 2.统计指令
ProblemSize = 1000
print('{0:<13}{1:<16}'.format('ProbleSize', 'Iterations'))
for count in range(5):
    
    number = 0
    # 算法开始
    work = 1
    for x in range(ProblemSize):
        for y in range(ProblemSize):
            number += 1
            work += 1
            work -= 1
    # 算法结束
    
    print('{0:<13}{1:<16}'.format(ProblemSize, number))
    ProblemSize *= 2
"""
结果
ProbleSize   Iterations      
1000         1000000         
2000         4000000         
4000         16000000        
8000         64000000        
16000        256000000
"""

from counter import Counter
def fib(n,counter):
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n - 1, counter) + fib(n -2, counter)

problemSize = 2
print('{0:12}{1:15}'.format('ProblemSize', 'Calls'))
for count in range(5):
    counter = Counter()

    # start
    fib(problemSize,counter)
    # end

    print('{0:<12}{1:<15}'.format(problemSize, str(counter)))
    problemSize *= 2
"""
结果
ProblemSize Calls          
2           1              
4           5              
8           41             
16          1973           
32          4356617
"""
# 统计指令是正确的思路，但是，你需要求助于逻辑和数学推理，才能有一个完整的分析方法。对于这种类型的分析，你所需要的工具只是纸和笔。
---------------------------------------------------------------------------------------------------------------------------------
# 3.度量算法所使用的内存
# 一些算法对于解决任何问题都需要相同大小的内存。而另一些算法则会随着问题规模越来越大，从而需要更多的内存。
