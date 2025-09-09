# <49>字符查找-找出第一个只出现一次的字符，没有则返回-1-----------------------------------------
# 先考虑使用字典计数
string = str(input("输入字符串:\n"))
dict = {}
flag = -1                            # 这个flag的思路不错

for i in string:
    if i in dict:
        dict[i] += 1                 # 字典存在该键则值加一
    else:
        dict[i] = 1                  # 不存在则创建该键并赋值1

print(dict)

for j in dict:
    if dict[j] == 1:                 # 遍历字典若值为1则输出对应键
        flag = j                     # 也可遍历原字符串，找到第一个计数为 1 的字符
        break

print(flag)