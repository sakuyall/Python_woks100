# <52>将字符串中空格替换为%---------------------------------------------------------------------
# 可参考字符串格式化一节
# 现在这个方法是迭代替换
def swap(s):
    save = ""
    for i in s:
        if i != " ":
            save += i
        else:
            save += "%"
    
    return save

print(swap("hello world"))