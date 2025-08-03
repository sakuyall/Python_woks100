# <5>求阶乘-------------------------------------------------------------------
num = 5                                 # 非递归方法(for循环)
sub = 1
for i in range(1,num + 1):
    sub *= i
print(sub)

def jie_cheng(num):                     # 递归方法(多次调用)
    if num == 1:
        return 1
    else:
        return num * jie_cheng(num - 1)
jie_cheng(5)
