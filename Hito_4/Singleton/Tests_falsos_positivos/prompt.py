# Crea 30 ejemplos de código en Python que parezcan implementar el patrón Singleton pero que en realidad sean falsos positivos.

# Los ejemplos deben:

# Incluir clases llamadas Singleton, MySingleton, Database, Logger u otras típicas de Singleton.

# Tener métodos o atributos típicos como _instance, get_instance(), __new__(), etc.

# Simular el Singleton pero con errores como:

# El Singleton no restringe múltiples instancias.

# get_instance() crea una nueva instancia cada vez.

# El atributo _instance nunca se utiliza.

# Mal uso de __new__() sin control de instancia.

# Herencias que rompen el Singleton.

# Variar en dificultad:

# Ejemplos muy simples con Singleton sin control de instancias.

# Ejemplos con variables de clase que parecen usarse para control de instancia pero no se usan correctamente.

# Los ejemplos deben ser sintácticamente correctos y ejecutables.

# Cada ejemplo de 10 a 30 líneas máximo.

# Cada ejemplo con título:

# shell
# Copiar
# Editar
# ### Ejemplo 1: Singleton sin control de instancia
# seguido del bloque de código.

# No expliques el error; solo genera el código.

# No incluyas explicaciones fuera de los ejemplos.

# El objetivo es probar detectores automáticos de patrones Singleton frente a falsos positivos.