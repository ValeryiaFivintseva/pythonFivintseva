from abc import ABC, abstractmethod
class CLothes(ABC):
    name = 'Leroy'
    print(f'Name of brand: {name}')
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
        elif size > 56:
            self.__size = 56
        else:
            self.__size = size

    def info(self):
        print(f'Size is {self.__size}')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 150:
            self.__height = 150
        elif height > 180:
            self.__height = 180
        else:
            self.__height = height

    def info2(self):
        print(f'Height is {self.__height}')

    @abstractmethod
    def paym(self):
        p1 = self.size / 6.5 + 0.5
        print(f'Material for create {p1}')


class Jacket(CLothes):
    def __init__(self, size):
        self.size = size

    def paym(self):
        p1 = self.size / 6.5 + 0.5
        print(f'Material for create Jacket {p1}')

J1 = Jacket(int(input('Size: ')))
J1.paym()
J1.info()
class Suit(CLothes):
    def __init__(self, height):
        self.height = height

    def paym(self):
        p2 = 2 * self.height + 0.3
        print(f'Material for create Suit {p2}')

S1 = Suit(int(input('Height: ')))
S1.paym()
S1.info2()


