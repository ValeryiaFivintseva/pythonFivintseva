with open(r'firms.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

with open(r'firms.txt', 'r', encoding='utf-8') as f:
        r = []
        r2 = []
        r = f.readlines()
        for i in r:
            r2.append(i.split(' '))
            # print(r, '\n')
            # print(r2)
        for i in r2:
            pr = int(i[2]) - int(i[3])
            print(i[0], '-', pr)
        count = 0
        summ = 0
        for i in r2:
            summ+= (int(i[2]) - int(i[3]))
            count+=1
            if (int(i[2]) - int(i[3])) < 0:
                count-= 1
                summ-= (int(i[2]) - int(i[3]))
                Sal = summ/count
                print(f'Средняя прибыль {Sal}')
        cmps = []
        average = {'average_profit': Sal}
        # print(average)
        cmps.append(average)
        for i in r2:
            com = {i[0]: int(i[2]) - int(i[3])}
            # print(com)
            cmps.append(com)
        print(cmps)
import json
with open('cmps.json', 'w', encoding='utf-8') as f:
        json.dump(cmps, f)















