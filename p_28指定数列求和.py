# <28>求指定数列的和2/1, 3/2, 5/3, 8/5, 13/8, ...前20项和-----------
sum = 0
up = 2
down = 1
for i in range(20):
    sum += up / down
    rec = up         # 储存起来
    up = up + down
    down = rec
print(sum)           # 32.66026079864164

# 尝试应用斐波那契数列 1 1 2 3 5...(任务完了)
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

sum = 0
for i in range(1,21):
    sum += fib(i + 1) / fib(i)

print(sum)           # 32.66026079864164