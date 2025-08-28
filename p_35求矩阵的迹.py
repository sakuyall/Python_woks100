# <35>求3*3矩阵的迹------------------------------------------------------
list = []

for i in range(3):
    list.append([])
    for j in range(3):
        k = int(input("输入数据"))         # 整型
        list[i].append(k)                 # 为大列表i位置的小列表添加元素

sum = 0
print("输入矩阵为：",list)

for i in range(3):
    for j in range(3):
        if i == j:
            sum += list[i][j]

print(sum)