# <37>给定两个变量，交换它们的值----------------
# 方法1
a = 1
b = 2
a,b = b,a    # 简单也可加中间变量折腾

# 方法2
def num_swap(a,b):
    list = []
    list.append(a)
    list.append(b)
    list[0],list[1] = list[1],list[0]
    return list

a = 1
b = 2
list = num_swap(a,b)
for i in list:
    print(i)