class TemperatureObserver:
    def update(self, temperature):
        pass

class Display(TemperatureObserver):
    def update(self, temperature):
        print(f"[Display] Showing temp: {temperature}°C")

class Alarm(TemperatureObserver):
    def update(self, temperature):
        if temperature > 30:
            print("[Alarm] WARNING: High temperature!")
