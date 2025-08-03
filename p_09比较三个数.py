# <9>比较三个数大小------------------------------------------------------------
a = int(input("输入第一个数:"))
b = int(input("输入第二个数:"))
c = int(input("输入第三个数:"))
list = [a,b,c]
list1 = sorted(list)                    # sorted排序
print(f"三个数字从小到大顺序为：{list1[0]},{list1[1]},{list1[2]}")
