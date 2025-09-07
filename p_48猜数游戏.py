# <48>猜数游戏----------------------------------------------------------
import random

target = random.randint(1,100)
times = 0

while times < 8:
    times += 1
    num = int(input("输入100内整数:\n"))

    if num == target:
        print("数字正确")
        break
    elif num > target:
        print(f"第{times}次,大了")
        continue
    elif num < target:
        print(f"第{times}次,小了")
        continue

if times == 8:
    print("机会用尽")