# <24>成绩90以上A，60以下C，其余B---------------------------------------
score = int(input("请输入成绩"))

if score >= 90:
    print("A")
elif 60 <= score < 90:
    print("B")
else:
    print("C")