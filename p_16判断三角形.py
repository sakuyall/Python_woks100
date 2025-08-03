# <16>输入三组数据，判断能否构成三角形-----------------------------------------
a = int(input("输入a边长"))
b = int(input("输入b边长"))
c = int(input("输入c边长"))
if a<=0 or b<=0 or c<=0:
    print("请输入正整数")
if a+b>c and b+c>a and a+c>b:
    print("可构成三角形")
else:
    print("不可构成")

# 使用列表索引来做
list = []
for i in range(3):
    num = int(input(f"请输入第{i+1}条边长"))  # 列表为空索引或超限会报错
    list.append(num)       # IndexError: list assignment index out of range
list.sort()
if list[0] + list[1] > list[2]:     # 直接用最小的两个加一起比较
    print("可构成三角形")
else:
    print("不可构成")