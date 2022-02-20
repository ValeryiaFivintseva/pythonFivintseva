def my_func(x, y):
    res = 1 / (x ** (abs(y)))
    return res
r = my_func(2, -4)
print (r)
#циклом:
def my_func(x = 2, y = -4):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y < 0:
        res = 1 / res
        print(f"{x} ** {y} == ", res)
my_func(x = 2, y = -4)
