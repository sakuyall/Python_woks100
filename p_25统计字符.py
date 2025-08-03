# <25>统计字符串中指定字符数----------------------------------------------
string = input("请输入字符串：")

word = 0           # 字母，数字，空格，其他出现次数
num = 0
space = 0
other = 0

for i in string:
    if i.isalpha():
        word += 1
    elif i.isdigit():
        num += 1
    elif i.isspace():
        space += 1
    else:
        other += 1

print(f"英文字母有{word}个，数字有{num}个，空格有{space}个，其他有{other}个。")

# 值得注意的是，中文汉字会被isalpha识别为True，判断中文可按照unicode范围
# python3.0后所有字符串均为支持unicode的u字符串
# 中文的范围为：['/u4e00'，'/u9fa5']