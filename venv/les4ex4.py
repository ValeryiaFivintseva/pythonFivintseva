# нужно через инпут
from random import random
sp = []
for j in range(10):
    sp.append(int(random()*10))
print(sp)
sp2 = [i for i in sp if sp.count(i) == 1]
print(sp2)