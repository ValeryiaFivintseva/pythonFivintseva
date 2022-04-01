# ЗДЕСЬ БУДУТ ЗАДАНИЯ С 4 ПО 6; Я РЕШИЛА СДЕЛАТЬ СКЛАД ЛЕКАРСТВ
# ВСЁ С ВВОДОМ ДАННЫХ ОТ ПОЛЬЗОВАТЕЛЯ, ТАК ЧТО..ТЕРПЕНИЯ;)
from abc import ABC, abstractmethod
class StoreMedicine(ABC):
    def __init__(self, pac, price, prod):
        self.pac = pac
        self.price = price
        self.prod = prod
        print(f'количество упаковок на складе - {self.pac}, общ.сумма - {self.price} $, страна(ы) изгот. - {self.prod}')
    @abstractmethod
    def get_med(self):
        n = input('Кол-во упаковок принятых на склад: ')
        print(f'{n} упаковок принято на склад')
    @abstractmethod
    def transfer(self):
        class OnlyNumbers(Exception):
            def __init__(self, txt):
                self.txt = txt

        while True:
            try:
                co = input('Укажите кол-во передаваемых упаковок: ')
                if co.isdigit():
                    print(f'{co} упаковок передано в аптеку №')
                elif isinstance(co, str):
                    raise OnlyNumbers('Only numbers, please')
            except OnlyNumbers as err:
                print(err)
            if co.isdigit():
                break
# Я подумала о методе __str__ для создания словаря для хранения данных, но подозреваю, что возможно не поняла условия
    def __str__(self):
        i = {'количество упаковок': f'{self.pac}', 'цена': f'{self.price} $', 'производитель': f'{self.prod}'}
        return f'Лекарственные средства: {i}'
class Pil(StoreMedicine):
    def __init__(self, pac, price, prod, form):
        super().__init__(pac, price, prod)
        self.form = form
        print(f'форма таблеток - {self.form}')
    def get_med(self):
        n = input('Кол-во упаковок таблеток принятых на склад: ')
        print(f'{n} упаковок таблеток принято на склад')

    def transfer(self):
        class OnlyNumbers(Exception):
            def __init__(self, txt):
                self.txt = txt

        while True:
            try:
                co = input('Укажите кол-во передаваемых упаковок таблеток: ')
                if co.isdigit():
                    print(f'{co} упаковок таблеток передано в аптеку №1')
                elif isinstance(co, str):
                    raise OnlyNumbers('Only numbers, please')
            except OnlyNumbers as err:
                print(err)
            if co.isdigit():
                break

    def __str__(self):
        i = {'количество упаковок': f'{self.pac}', 'цена': f'{self.price} $',
             'производитель': f'{self.prod}', 'форма табл.': f'{self.form}'}
        return f'Таблетки: {i}'
class Pulv(StoreMedicine):
    def __init__(self, pac, price, prod, weight):
        super().__init__(pac, price, prod)
        self.weight = weight
        print(f'вес субстанции - {self.weight}')
    def get_med(self):
        n = input('Кол-во упаковок порошков принятых на склад: ')
        print(f'{n} упаковок порошков принято на склад')

    def transfer(self):
        class OnlyNumbers(Exception):
            def __init__(self, txt):
                self.txt = txt

        while True:
            try:
                co = input('Укажите кол-во передаваемых упаковок порошков: ')
                if co.isdigit():
                    print(f'{co} упаковок порошков передано в аптеку №2')
                elif isinstance(co, str):
                    raise OnlyNumbers('Only numbers, please')
            except OnlyNumbers as err:
                print(err)
            if co.isdigit():
                break
    def __str__(self):
        i = {'количество упаковок': f'{self.pac}', 'цена': f'{self.price} $',
             'производитель': f'{self.prod}', 'общ.вес субстанции': f'{self.weight}'}
        return f'Порошки: {i}'
class Sol(StoreMedicine):
    def __init__(self, pac, price, prod, intro):
        super().__init__(pac, price, prod)
        self.intro = intro
        print(f'раствор вводить - {self.intro}')
    def get_med(self):
        n = input('Кол-во упаковок ампул принятых на склад: ')
        print(f'{n} упаковок ампул принято на склад')

    def transfer(self):
        class OnlyNumbers(Exception):
            def __init__(self, txt):
                self.txt = txt

        while True:
            try:
                co = input('Укажите кол-во передаваемых упаковок ампул: ')
                if co.isdigit():
                    print(f'{co} упаковок ампул передано в аптеку №3')
                elif isinstance(co, str):
                    raise OnlyNumbers('Only numbers, please')
            except OnlyNumbers as err:
                print(err)
            if co.isdigit():
                break
    def __str__(self):
        i = {'количество упаковок': f'{self.pac}', 'цена': f'{self.price} $',
             'производитель': f'{self.prod}', 'способ введения': f'{self.intro}'}
        return f'Растворы: {i}'
kt = input('Кол-во упак.таблеток на складе: ')
st = input('На сумму в $: ')
ct = input('Страна(ы) изгот.: ')
f = input('Форма табл.: ')
kp = input('Кол-во упак.порошков на складе: ')
sp = input('На сумму в $: ')
cp = input('Страна(ы) изгот.: ')
w = input('Общ.вес порошк.субстанции в кг: ')
ks = input('Кол-во упак. ампул на складе: ')
ss = input('На сумму в $: ')
cs = input('Страна(ы) изгот.: ')
v = input('Способ введения раствора: ')
P1 = Pil(kt, st, ct, f)
Pl1 = Pulv(kp, sp, cp, w)
S1 = Sol(ks, ss, cs, v)
print(P1)
P1.get_med()
P1.transfer()
print(Pl1)
Pl1.get_med()
Pl1.transfer()
print(S1)
S1.get_med()
S1.transfer()