class Road:
    _length = 100
    _width = 50
    def __init__(self, _length, _width):
        self.l = _length
        self.w = _width
        paym = self.l * self.w * 25 * 0.005
        print(f'Масса асфальта: {paym} т')
Asphalt = Road(100, 50)

