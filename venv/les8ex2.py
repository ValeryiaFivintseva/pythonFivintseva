class Del(Exception):
    def __init__(self, txt):
        self.txt = txt
try:
    num = int(input('Number: '))
    num2 = int(input('Number: '))
    if num2 == 0:
        raise Del('Division by zero is impossible!')
    res = num / num2
except ValueError:
    print('Not a number')
except Del as err:
    print(err)
else:
    print(res)
finally:
    print('End of calculate')