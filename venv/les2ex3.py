se = {'win': [12, 1, 2], 'spr': [3, 4, 5], 'sum': [6, 7, 8], 'aut': [9,10,11]}
num = int(input())
for el in se:
    if num in se[el]:
        print(el)
