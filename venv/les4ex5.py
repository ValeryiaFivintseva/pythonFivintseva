my_li = [i for i in range(100 , 1001) if i % 2 == 0]
print(my_li)
from functools import reduce
def fin(x, y):
    return x * y
print(reduce(fin, my_li))