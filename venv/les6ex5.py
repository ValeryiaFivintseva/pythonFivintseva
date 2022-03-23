class Stationery:
    title = 'Канцелярские принадлежности'
    print(title)
    def draw(self):
        print('Запуск отрисовки')
Stat1 = Stationery()
Stat1.draw()
class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой')
Pen1 = Pen()
Pen1.draw()
class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')
Pencil1 = Pencil()
Pencil1.draw()
class Handle(Stationery):
    def draw(self):
        print('Выделяем маркером')
Handle1 = Handle()
Handle1.draw()