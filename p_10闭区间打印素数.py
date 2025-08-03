# <10>输入闭区间打印其中全部素数------------------------------------------------
def isprime(n):
    flag = True
    for i in range(2,n):
        if n % i == 0:
            flag = False
            break
    return flag

a = int(input("输入左区间"))
b = int(input("输入右区间"))
list = []

for i in range(a,b+1):
    if isprime(i) == True:
        list.apppend(i)
print(list)