from itertools import count
for el in count(int(input('Enter number for start: '))):
    print(el)
    if el == 12:
        break

s = [2, 5, 16, 22, 4, 8]
i = 0
from itertools import cycle
for el in cycle(s):
    print(el)
    i += 1
    if i > 10:
        break
