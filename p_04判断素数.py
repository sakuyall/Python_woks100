# <4>判断某数是否为素数--------------------------------------------------------
num = 3
flag = False
for i in range(2,num):                  # num为2时不循环，这里只考虑循环次数
    if num % i == 0:                    # 从2到它前一个数有没有能除的开的（效率低）
        flag = True                     # 只要出现可整除就为合数
        break
if flag:
    print("是合数")
else:
    print("是素数")