# <18>输入正整数输出它所有质数因子------------------------------------
num = int(input("输入一个自然数"))
x = 2
list = []

while num >= x:
    if num % x == 0:
        list.append(x)
        num /= x
    else:
        x += 1
for i in list:
    print(i,end=" ")