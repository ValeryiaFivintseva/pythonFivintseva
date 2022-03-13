with open(r'stroki.txt', 'r', encoding='utf-8') as f:
    st = f.readlines()
    print(len(st))
with open(r'stroki.txt', 'r', encoding='utf-8') as f:
    t1 = f.readline()
    print(t1.count(' ') + 1)
    t2 = f.readline()
    print(t2.count(' ') + 1)
    t3 = f.readline()
    print(t3.count(' ') + 1)
