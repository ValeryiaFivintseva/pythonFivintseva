def f_del(n, n2):
    try:
        res = n // n2
        return res
    except ZeroDivisionError:
        return 'num != 0'
r = f_del(n = float(input('Num1: ')), n2 = float(input('Num2: ')))
print(r)



