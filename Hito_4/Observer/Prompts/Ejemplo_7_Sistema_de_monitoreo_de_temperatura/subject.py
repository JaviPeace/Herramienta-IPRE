class TemperatureSensor:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def notify(self, temperature):
        for obs in self._observers:
            obs.update(temperature)

    def read_temperature(self, value):
        print(f"[Sensor] Temp is {value}°C")
        self.notify(value)
