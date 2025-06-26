from singleton_config import Singleton

a = Singleton("config.json")
b = Singleton()
print(a.config == b.config)  # True
print(a is b)                # True
