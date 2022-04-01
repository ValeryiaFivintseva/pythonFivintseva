class OnlyNumbers(Exception):
    def __init__(self, txt):
        self.txt = txt

s = []
while True:
    try:
        x = input('Please enter data: ')
        if x.isdigit():
            s.append(x)
            # print(s)
        elif isinstance(x, str):
            raise OnlyNumbers('Only numbers, please')
    except OnlyNumbers as err:
        print(err)
    if x == 'stop':
        print(s)
        break