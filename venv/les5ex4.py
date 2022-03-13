with open(r'ottf.txt', 'r', encoding='utf-8') as f:
        list = f.read().split('\n')
        for i in list:
            i = i.split()
            list[0] = 'Один - 1\n'
            list[1] = 'Два - 2\n'
            list[2] = 'Три - 3\n'
            list[3] = 'Четыре - 4\n'
        # print(list)
        print(list[0].strip())
        print(list[1].strip())
        print(list[2].strip())
        print(list[3].strip())
with open(r'ottf2.txt', 'w', encoding='utf-8') as f2:
     f2.writelines(list)



