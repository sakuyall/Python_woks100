# <17>找出1000内完数：等于除它以外的因子之和------------------------------------
for i in range(1,1000):
    list = []                    # 开始新一个数的因数寻找前更新列表
    for j in range(1,i):
        if i % j == 0:
            list.append(j)
    if sum(list) == i:
        print(f"发现{i}是完数")
