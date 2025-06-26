# Varias capas de decoradores

class Coffee:
    def cost(self):
        return 5

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5

# Uso
coffee = Coffee()
milk_coffee = MilkDecorator(coffee)
sugar_milk_coffee = SugarDecorator(milk_coffee)
print(sugar_milk_coffee.cost())  # 6.5
