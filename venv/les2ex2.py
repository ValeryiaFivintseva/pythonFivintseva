li = list(map(int, input('li: ').split()))
print('before: ', li)
li[0], li[1] = li[1], li[0]
li[2], li[3] = li[3], li[2]
print('after: ', li)