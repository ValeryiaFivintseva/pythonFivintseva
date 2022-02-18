my_list = [9, 7, 5, 3, 2]
print(my_list)
while True:
    n = int(input('Введите число: '))
    my_list.append(n)
    my_list = sorted(my_list, reverse = True)
    print(my_list)
    if n == 2:
        break




