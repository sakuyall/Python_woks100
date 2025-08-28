# <36.1>加入判断正负序完善，这是默认有序的情况下啊-----------------------------------------
# 1.考虑负序逆转后用正序方法
def flag(list):
    global length
    length = len(list)
    if list[0] < list[length - 1]:
        return True    # 正序
    else:
        return False   # 负序

def out_put():
    for i in range(length):
        if a < list[i]:                      # 若小于该位置则插入在它前边
            list.insert(i,a)                 # insert(插入位置，插入元素)
            break                            # 插入后就结束
        elif a > list[length - 1]:           # 若大于最后一个
            list.append(a)                   # 正序直接放最后
            break                            # 不再继续循环
    return list

list = [1,3,56,78,100]
# list = [100,78,56,3,1]
a = int(input("输入新数据"))

if flag(list):
    out_put()
    print(list)
else:
    list = list[::-1]         # 负序转正序
    out_put()
    list = list[::-1]         # 转回来
    print(list)

# 可额外搜索判断列表是否有序的方法