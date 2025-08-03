# <15>输入字符，判断是否为字母-----------------------------------------
a = input('输入')
result = a.isalpha()     # 判断字母返回布尔值TF
if result:
    print("是字母")
else:
    print("不是字母")