# <21>找出斐波那契数列第n项----------------------------------------------------
# 递归方法:函数自我调用且有终止条件
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(6))
    
# 非递归复杂度高
n = 6
fibs = [1,1]
for i in range(2,n + 1):
    num = fib[i - 2] + fib[i - 1]
    fib.append(num)
print(list[n - 1])