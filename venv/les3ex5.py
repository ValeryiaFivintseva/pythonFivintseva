def m_f():
    sum = 0
    n = False
    while n == False:
        number = input('numbers or press Enter for exit: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == '&':
                n = True
                break
            else:
                res = res + int(number[el])
        sum = sum + res
        print(f'sum is {sum}')
    print(f'final sum is {sum}')
m_f()







