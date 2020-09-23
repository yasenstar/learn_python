# 列出100内的所有质数 (老师的做法)
# 模块，通过模块进行扩展
# 引入一个time模块，来统计程序执行的时间，返回单位是秒
from time import *

begin = time()

i = 2
while i <= 50:
    flag = True
    j = 2
    while j <= i ** 0.5:
        if (i % j) == 0:
            # print ("不是质数")
            flag = False
            # 一旦进入判断，则证明一定不是质数
            break
        j += 1
    if flag:
        print(i, " ", end="")
    i += 1
print()

end = time()

print("程序执行花费了： ", end-begin)

