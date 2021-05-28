# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе
# определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

class OfficeWarehouse:
    def __init__(self, name, price, color, amount):
        self.name = name
        self.price = price
        self.color = color
        self.amount = []


class OfficeEquipment:
    def __init__(self, name, price, color, amount):
        self.name = name
        self.price = price
        self.color = color
        self.amount = []


class Printer(OfficeEquipment):
    def __init__(self, name, price, color, amount, size):
        super().__init__(name, price, color, amount)
        self.size = size

class Scanner(OfficeEquipment):
    def __init__(self, name, price, color, amount, shape):
        super().__init__(name, price, color, amount)
        self.shape = shape


class Xerox(OfficeEquipment):
    def __init__(self, name, price, color, amount, position):
        super().__init__(name, price, color, amount)
        self.position = position