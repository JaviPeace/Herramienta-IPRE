from subject import TemperatureSensor
from observer import Display, Alarm

sensor = TemperatureSensor()
sensor.register(Display())
sensor.register(Alarm())

sensor.read_temperature(25)
sensor.read_temperature(35)
