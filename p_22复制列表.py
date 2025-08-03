# <22>复制列表----------------------------------------------------
list = [1,2,3,4]
list1 = list          # 浅拷贝，改list后list1也会变化
print(list1)

import copy
list = [1,2,3,4]
list1 = copy.copy(list)      # 深拷贝，不会变化，应该也可用for循环