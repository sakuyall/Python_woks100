# <27>猴子吃桃问题 一天摘下若干桃子，一天吃一半多一个，第十天只剩一个，求第一天有多少-----------
# for循环迭代方法
num = 1
for i in range(9):
    num += 1
    num *= 2
print(num)         #1534个

# 函数递归方法
def total(n):
    if n == 10:
        return  1
    if n < 10:
        return (total(n + 1) + 1 ) * 2   # 注意先后顺序
    
print(total(1))   # 1534个