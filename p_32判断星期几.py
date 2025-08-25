# <32>输入英文星期判断星期几-感觉意义不大-------------------------------------------------------
a = input("输入第一个字母")

if a == "M":
    print("周一")

elif a == "T":
    b = input("请输入第二个字母")
    if b == "u":
        print("是周二")
    elif b == "h":
        print("是周四")
        
elif a == "W":
    print("是周三")

elif a == "F":
    print("是周五")

elif a == "S":
    b = input("请输入第二个字母")
    if b == "a":
        print("是周六")
    elif b == "u":
        print("是周日")

else:
    print("输入错误")