# <51>补充数组-----------------------------------------------------------------------
# 给定长度为n的数组，找出数组中在[1，n]中未出现过的数字并添加到其中
# 比如输入[2,1,1,4,5,5],返回[3,6]
def func(nums):
    l = [i for i in range(1,len(nums) + 1)]   # 长度为n完整列表
    l2 = []
    nums = set(nums)        # 转为集合消除重复元素
    for j in l:
        if j in nums:
            continue
        else:
            l2.append(j)

    return l2

print(func([1,2,3,5,5]))