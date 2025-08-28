# <36>有序列表添加数据，有一排好序的列表，输入一个数将其按原有规律插入----------------
def swap_Position(list,pos1,pos2):                 # 这个没用到
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list

list = [1,3,56,78,100]        # 首先以正序为例----------------------------------
before_length = (len(list))

a = int(input("输入新数据"))

for i in range(before_length):
    if a < list[i]:                           # 若小于该位置则插入在它前边
        list.insert(i,a)                      # insert(插入位置，插入元素)
        break                                 # 插入后就结束
    elif a > list[before_length - 1]:         # 若大于最后一个
        list.append(a)                        # 正序直接放最后
        break                                 # 不再继续循环
print(list)
