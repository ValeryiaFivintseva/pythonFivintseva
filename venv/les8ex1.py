class Data:
    def __init__(self, day):
        self.day = day
        # print(self.day)

    @classmethod
    def my_method(cls, data):
        d = data
        print(f'{int(d[0:2])}.{int(d[3:5])}.{int(d[6:10])}')
        return cls(d)

    @staticmethod
    def valide(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

st = '12.11.2007'
D1 = Data.my_method(st)
print(Data.valide(12, 11, 2007))



