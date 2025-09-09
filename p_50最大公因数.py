# <50>求两数最大公因数-----------------------------------------------------------------------
def func1(a,b):
    if a == b:
        return a
    num = min(a,b)
    while a % num != 0 or b % num != 0:
        num -= 1
    return num

def func2(a,b):                  # 辗转相除法,分母不为0
    while b != 0:
        a, b = b, a % b
    return a

print(func1(12,25))
print(func2(12,18))