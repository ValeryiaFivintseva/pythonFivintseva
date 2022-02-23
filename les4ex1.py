from sys import argv
print(argv)
print("Имя скрипта: ", argv[0])
print("Часы: ", argv[1])
print("Ставка в час: ", argv[2])
print("Премия: ", argv[3])
m = [int(x) for x in argv[1 : ]]
print(m)
def money():
    a = m[0]
    b = m[1]
    c = m[2]
    salary = (a * b) + c
    return salary
s = money()
print(s)