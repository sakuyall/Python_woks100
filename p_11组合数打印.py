# <11>组合数字1234组合多少无重复三位数并打印--------------------------------------
list = []
for i in range(1,5):
    for j in range(1,5):
            for k in range(1,5):
                if (i != j) & (i != k) & (j != k):
                    num = i * 100 + j * 10 + k       # 或者f字符串拼写f“{i}{j}{k}”
                    list.append(num)
print(list)