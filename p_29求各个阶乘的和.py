# <29>求各个阶乘的和1到20-----------
def jie_cheng(n):
    if n == 0:
        return 1
    else:
        return jie_cheng(n - 1) * n

sum = 0
for i in range(1,21):
    sum += jie_cheng(i)

print(sum)                              # 2561327494111820313

# 或者更简单的方法：
import math

sum = 0
for i in range(1,21):
    sum += math.factorial(i)

print(sum)                              # 2561327494111820313