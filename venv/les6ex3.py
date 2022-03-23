class Worker:
    def __init__(self, name, surname, position, _income):
        self.n = name
        self.surn = surname
        self.p = position
        self._i = _income

class Position(Worker):
    def get_full_name(self):
        print(f'{self.n} {self.surn}')
    def get_total_income(self):
        print(self._i["wage"] + self._i["bonus"])
position1 = Position('Alex', 'Filger', 'manager', {"wage": 2500, "bonus": 1000})
position1.get_full_name()
position1.get_total_income()

# Я ПОНИМАЮ, ЧТО ДЛЯ УНИВЕРСАЛЬНОСТИ, ЗНАЧЕНИЯ МОЖНО ЗАДАТЬ ЧЕРЕЗ ИНПУТ. ПРОСТО ДЕЛАЮ СРАЗУ НАГЛЯДНО