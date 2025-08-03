# <13>取100-999的水仙花数:各位立方和等于其本身-------------------------------------
import math
for i in range(100,1000):
    a = i % 10                # 个位
    b = (i % 100) // 10       # 十位
    c = i // 100              # 百位
    if pow(a,3) + pow(b,3) + pow(c,3) == i:
        print(f'{c}{b}{a}是水仙花数')

# 或者用字符串获取
import math
for i in range(100,1000):
    i = str(i)
    a = i[0]
    b = i[1]
    c = i[2]
    a = int(a)
    b = int(b)
    c = int(c)
    i = int(i)               # 注意要转换回去
    if pow(a,3) + pow(b,3) + pow(c,3) == i:
        print(f'{i}是水仙花数')