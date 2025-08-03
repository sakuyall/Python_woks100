# <19>海伦公式求三角形面积---------------------------------------------
import math
list = []

for i in range(3):
    num = int(input(f"输入三角形第{i+1}条边长"))
    list.append(num)
p = sum(list) / 2
S = math.sqrt(p * (p - list[0]) * (p - list[1]) * (p - list[2]))
print(f"求得三角形面积为{S}")