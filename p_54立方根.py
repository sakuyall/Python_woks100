# <54>立方根，给定正整数开立方根，向下取整----------------------------------------
import math

def func():
    n = int(input("输入正整数:\n"))
    result = math.pow(n,1/3)
    return int(result)                # 利用int整形直接实现向下取整

print(func())