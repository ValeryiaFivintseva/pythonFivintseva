n = int(input('Введите целое число: '))
def fact(n):
    p = 1
    for i in range(1, n + 1):
        p = p * i
        yield p
for i in fact(n):
    print(i, end= ' ')