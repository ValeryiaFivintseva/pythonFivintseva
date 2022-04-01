class ComNum:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return self.num + other.num
    def __sub__(self, other):
        return self.num - other.num
    def __mul__(self, other):
        return self.num * other.num
    def __truediv__(self, other):
        return self.num / other.num

a = 3 + 4j
b = 2 + 2j
C1 = ComNum(a)
C2 = ComNum(b)
print(C1 + C2)
print(C1 - C2)
print(C1 * C2)
print(C1 / C2)

