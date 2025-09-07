# <40>温度转换，在正课应该写过------------------------
def Temperature_C2F(C):
    return 1.8 * C + 32

def Temperature_F2C(F):
    return (F - 32) / 1.8

flag = int(input("摄氏度请按1,华氏度请按2"))
num = float(input("请输入温度"))

if flag == 1:
    print(f"华氏温度为：{Temperature_C2F(num)}℉",)
elif flag == 2:
    print(f"摄氏温度为：{Temperature_F2C(num)}℃",)
else:
    print("非法输入")