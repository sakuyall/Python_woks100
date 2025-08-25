# <30>年龄递减问题-第五个往前依次递减两岁，第一个人10岁问第五个多少岁-----------
def age(n):
    if n == 1:
        return 10
    else:
        return age(n - 1) + 2
    
print(age(5))                     # 刚满十八岁(