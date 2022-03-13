# НЕ ПОНИМАЮ, ПОЧЕМУ ТАК НЕ РАБОТАЕТ. ВНОСИТ В СПИСОК SAL ЦИФРЫ ПООЧЕРЕДНО, А НЕ ВСЕ СРАЗУ
# with open(r'oklad.txt', 'r', encoding='utf-8') as f:
#     sal = []
#     wr = {}
#     for line in f:
#         key, value = line.split()
#         wr[key] = value
#         if float(value) < 20000.00:
#             print(f'{key}: salary less than 20000.00')
#         sal.append(value)
#           print(f'средний оклад {sum(map(float, sal)) / len(sal)}')




with open(r'oklad.txt', 'r', encoding='utf-8') as f:
    sal = []
    litsal = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000.00:
           litsal.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20000.00 {litsal}, средний оклад {sum(map(float, sal)) / len(sal)}')

