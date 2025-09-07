# <41,42,43,44>按位运算------------------------
print(3 & 5)                   # 二进制位与操作也是&，位或是|,位异或^

# 按照原理十进制转二进制
bin = []
num = int(input("输入十进制数"))
binstring = ""

while num > 0:
    rem = num % 2        # 取余数
    num = num // 2       # 商继续除以2
    bin.append(rem)      # 存入列表

while len(bin) > 0:
    binstring += str(bin.pop())     # 结合pop函数，栈的逻辑后进先出

print(binstring)

# 取反操作：八位二进制数符号位为1表负，用正数取反加一得到负数的补码
# 数电已经忘干净了……

# 45为len函数及迭代累加求取字符串长度，省略