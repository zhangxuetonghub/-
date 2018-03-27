# 1.度量算法的运行时间
import time
ProblemSize = 10000000
print('{0:<13}{1:<16}'.format('ProbleSize', 'Seconds'))
for count in range(5):
    
    start = time.time()
    # 算法开始
    work = 1
    for x in range(ProblemSize):
        work += 1
        work -= 1
    # 算法结束
    elapsed = time.time() - start
    
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
