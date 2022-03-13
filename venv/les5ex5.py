with open(r'numbs.txt', 'x', encoding='utf-8') as f:
    f.write('4 8 12 20 25 44')
with open(r'numbs.txt', 'r', encoding='utf-8') as f:
    r = f.read().split()
    # print(r)
    res = sum(map(int, r))
    print(res)