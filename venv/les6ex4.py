# Я РЕШИЛА ДАТЬ ВОЗМОЖНОСТЬ ПОЛЬЗОВАТЕЛЮ УКАЗЫВАТЬ МАРКУ АВТО И Т.Д., ЧТОБЫ РАБОТАЛО УНИВЕРСАЛЬНО
# ПРОГРАММА ВЫШЛА БОЛЬШАЯ И ДОЛГАЯ:)
class Car:
    def __init__(self, speed, color, name, is_police):
        self.s = speed
        self.c = color
        self.n = name
        self.i_p = is_police
        print(self.s, self.c, self.n, self.i_p)
    def go(self):
        print('Car is going')
    def stop(self):
        print('Car stoped')
    def turn(self):
        print('Car turned right')
    def show_speed(self):
        print(int(input('Speed is: ')))
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
    def show_speed(self):
        sp = int(input('Speed again: '))
        count = 0
        while count <= 1:
            if sp > 60:
                print('Speed overhight!!!')
            elif sp <= 60:
                print('Speed is normal')
            break
tcar1 = TownCar(input('Speed km/h: '), input('Color: '), input('Name: '), 'is_police - False(TownCar)')
tcar1.go()
tcar1.show_speed()
tcar1.turn()
tcar1.stop()
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
    def show_speed(self):
        sk = int(input('Speed again: '))
        count = 0
        while count <= 1:
            if sk > 40:
                print('Speed overhight!!!')
            elif sk <= 40:
                print('Speed is normal')
            break
wcar1 = WorkCar(input('Speed km/h: '), input('Color: '), input('Name: '), 'is_police - False(WorkCar)')
wcar1.go()
wcar1.show_speed()
wcar1.turn()
wcar1.stop()

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
scar1 = SportCar(input('Speed km/h: '), input('Color: '), input('Name: '), 'is_police - False(SportCar)')
scar1.go()
scar1.show_speed()
scar1.turn()
scar1.stop()

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
pcar1 = PoliceCar(input('Speed km/h: '), input('Color: '), input('Name: '), 'is_police - True(PoliceCar)')
pcar1.go()
pcar1.show_speed()
pcar1.turn()
pcar1.stop()
