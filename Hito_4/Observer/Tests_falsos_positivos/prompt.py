# Crea 30 ejemplos de código en Python que parezcan utilizar el patrón Observer pero que en realidad sean falsos positivos.

# Los ejemplos deben:

# Incluir clases llamadas Subject, Observer, ConcreteObserver, ConcreteSubject, Publisher, Subscriber, etc.

# Tener métodos típicos como attach(), detach(), notify(), update().

# Simular la estructura del patrón Observer, pero con fallas como:

# Subject no mantiene una lista de observadores.

# notify() existe pero no llama a update() en observadores.

# Observer implementa update(), pero Subject nunca los llama.

# Uso de nombres correctos pero estructura incompleta.

# Variar en dificultad:

# Ejemplos muy simples.

# Ejemplos con múltiples métodos pero con errores sutiles de diseño.

# Los ejemplos deben ser sintácticamente correctos y ejecutables.

# Cada ejemplo de 10 a 30 líneas máximo.

# Cada ejemplo con título:

# shell
# Copiar
# Editar
# ### Ejemplo 1: Subject sin lista de observadores
# seguido del bloque de código.

# No expliques el error; solo genera el código.

# No incluyas explicaciones fuera de los ejemplos.

# El objetivo es entrenar y probar sistemas de detección automática de patrones frente a falsos positivos que superficialmente parecen Observer.