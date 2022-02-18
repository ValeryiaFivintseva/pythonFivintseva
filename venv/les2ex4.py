while True:
    st = input('Введите фразу с пробелами: ').split()
    print(st)
    if str == 'university' or 'университет':
        break
for i, word in enumerate(st, 1):
    print(i, word)
n = len(word)
if n >= 10:
    print(word[0:10])





