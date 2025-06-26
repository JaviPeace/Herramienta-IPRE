class Observer:
    def __init__(self, condition):
        self.condition = condition

    def update(self, value):
        if self.condition(value):
            print(f"Condition met with value {value}")

class Sensor:
    def __init__(self):
        self.listeners = []

    def register(self, obs):
        self.listeners.append(obs)

    def new_value(self, value):
        for l in self.listeners:
            l.update(value)

# Uso
sensor = Sensor()
sensor.register(Observer(lambda x: x > 50))
sensor.new_value(30)  # nada
sensor.new_value(60)  # se imprime
