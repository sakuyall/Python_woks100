# <26>球从100米落下，落地后反弹原高度一半，求n次落地时经过多少米与反弹高度--------
# 先自己写一个
vertigo = 100
times = int(input("输入反弹次数"))
xlist = []

for i in range(0,times):
    xlist.append(vertigo)
    vertigo /= 2
    xlist.append(vertigo)

print(xlist.pop())      # pop函数提取出指定索引元素，默认为最后一个
print(sum(xlist))

# 递归方法
import math
def fall_routes(heigh,time):
    while time > 0:
        if time == 1:
            return heigh / 2        # 返回一次反弹路程与下次反弹高度
        elif time > 1:
            return fall_routes(heigh,time - 1) + heigh / pow(2,time - 1)

fall_routes(100,2)
# ??????????????????????????????????????????????学完函数的
