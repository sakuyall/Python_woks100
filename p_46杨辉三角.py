# <46>杨辉三角-每个数字是头顶两数之和-------------------------------------------------------------
def yanghui(list, i, j):                                  # i行j列元素值
    while i >= j:                                         # 先判断下三角形状
        if len(list) < 2 or j == 0 or i == j:
            return 1                                      # 三行以内返回元素1,对角线及第一列返回1
        else:                                             # 等于2时就已经在输入第三行内容了,不能写3
            return list[i - 1][j] + list[i - 1][j - 1]    # 其他位置返回上行两数相加

list = []

for i in range(0,10):
    list.append([])                                       # 每次新开一行
    for j in range(0,10):
        if i >= j:
            list[i].append(yanghui(list,i,j))             # 子列表内加本行元素

for row in list:
    print(row)

# 也可考虑先创建10*10全0矩阵