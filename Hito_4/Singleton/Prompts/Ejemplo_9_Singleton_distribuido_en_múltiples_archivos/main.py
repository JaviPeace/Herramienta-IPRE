from logger import Logger

a = Logger()
b = Logger()
a.log("Mensaje 1")
print(b.messages)  # ['Mensaje 1']
print(a is b)      # True
