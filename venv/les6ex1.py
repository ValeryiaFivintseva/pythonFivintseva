# ПЕРВАЯ ВЕРСИЯ. РАБОТАЕТ, НО НЕ ПОЛУЧИЛОСЬ ПРИДУМАТЬ ЦИКЛ ЗАВЕРШЕНИЯ --> РАБОТАЕТ БЕСКОНЕЧНО:))

# import time
# class TrafficLight:
#     __colors = ['красный', 'желтый', 'зеленый']
#
#     def running(self):
#         c = ['красный', 'желтый', 'зеленый']
#         for c[0] in c:
#             print(c[0])
#             time.sleep(7)
#         for c[1] in c:
#             print(c[1])
#             time.sleep(2)
#         for c[2] in c:
#             print(c[2])
#             time.sleep(5)
# svetofor = TrafficLight()
# svetofor.running()

# ПРИШЛО В ГОЛОВУ, КАК ОСТАНОВИТЬ И ВОТ ЛУЧШЕ:

from time import sleep
class TrafficLight:
    __colors = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        i = 0
        while i < 3:
            print(f'Переключение \n '
                  f'{TrafficLight.__colors[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1
TrafficLight = TrafficLight()
TrafficLight.running()