# ОБА КОДА РАБОТАЮТ, ЕСЛИ В ФАЙЛЕ НА МЕСТЕ ЦИФРЫ 0, А НЕ ПРОЧЕРК. С ПРОЧЕРКОМ НИКАК НЕ РАБОТАЕТ
# И СПИСКАМИ С ЦИКЛАМИ ДОБРАТЬСЯ ДО ПРОЧЕРКА, ЧТОБ НЕ ВКЛЮЧАТЬ ЕГО В СЧЕТ НЕ ПОЛУЧАЛОСЬ
with open(r'subjects.txt', 'r', encoding='utf-8') as f:
    sub = {}
    for line in f:
        subj, lect, l, practice, pr, labor, lab = line.split()
        sub[subj] = int(lect) + int(practice) + int(labor)
    print(sub)


with open(r'subjects2.txt', 'r', encoding='utf-8') as f:
    sub = []
    kol = []
    li = f.read().split('\n')
    # print(li)
    for i in li:
        r1 = li[0].split()
    # print(r1)
    r2 = li[1].split()
    # print(r2)
    r3 = li[2].split()
    # print(r3)
    sub.append(r1[0])
    sub.append(r2[0])
    sub.append(r3[0])
    # print(sub)
    kol.append(r1[1:8:3])
    kol.append(r2[1:8:3])
    kol.append(r3[1:8:3])
    # print(kol)
    res = [sum(map(int, kol[0])), sum(map(int, kol[1])), sum(map(int, kol[2]))]
    # print(res)
    d = {}
    d = dict(zip(sub, res))
    print(d)



