class Component:
    def get_total_price(self):
        raise NotImplementedError()

class Hammer(Component):
    def get_total_price(self):
        return 10  # ejemplo

class Phone(Component):
    def get_total_price(self):
        return 300  # ejemplo

class Headphones(Component):
    def get_total_price(self):
        return 50  # ejemplo

class Charger(Component):
    def get_total_price(self):
        return 25  # ejemplo

class Receipt(Component):
    def get_total_price(self):
        return 0  # ejemplo

class Box(Component):
    def __init__(self):
        self.contents = []

    def add(self, component):
        self.contents.append(component)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.contents)

class Iterator:
    def __init__(self, components):
        self._components = components
        self._index = 0

    def has_more(self):
        return self._index < len(self._components)

    def get_next(self):
        item = self._components[self._index]
        self._index += 1
        return item

class Controller:
    @staticmethod
    def create_order():
        hammer = Hammer()
        phone = Phone()
        headphones = Headphones()
        charger = Charger()
        receipt = Receipt()

        box1 = Box()
        box2 = Box()
        box3 = Box()
        box4 = Box()
        complete_order = Box()

        box1.add(hammer)
        box3.add(phone)
        box3.add(headphones)
        box4.add(charger)
        box2.add(box3)
        box2.add(box4)

        complete_order.add(box1)
        complete_order.add(box2)
        complete_order.add(receipt)

        return complete_order

    @staticmethod
    def get_price_list_using(iterator):
        list_of_prices = []
        while iterator.has_more():
            list_of_prices.append(iterator.get_next().get_total_price())
        return list_of_prices
