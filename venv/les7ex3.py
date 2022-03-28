class Cell:
    def __init__(self, kol):
        self.kol = kol
    def __add__(self, other):
        return self.kol + other.kol
    def __sub__(self, other):
        return self.kol - other.kol
    def __mul__(self, other):
        return self.kol * other.kol
    def __truediv__(self, other):
        return self.kol / other.kol
    # В задании было еще и целочисленное деление, поэтому я добавила метод из подсказок по ссылкам:
    def __floordiv__(self, other):
        return self.kol // other.kol
    def make_order(self, cells):
        w = ''
        for i in range(int(self.kol / cells)):
            w += f'{"*" * cells}\\n'
        w += f'{"*" * (self.kol % cells)}'
        print(w)
C1 = Cell(10)
C2 = Cell(4)
print(C1 + C2)
print(C1 - C2)
print(C1 * C2)
print(C1 / C2)
print(C1 // C2)
C1.make_order(5)
C2.make_order(3)
