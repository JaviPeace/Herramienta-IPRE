# Crea 30 ejemplos de código en Python que parezcan utilizar el patrón de diseño Composite pero que en realidad sean falsos positivos.

# Los ejemplos deben:

# Incluir clases llamadas Component, Leaf, Composite o similares para simular que están implementando Composite.

# Tener métodos con nombres típicos de Composite como operation(), add(), remove(), render(), cost(), etc.

# Variar en dificultad:

# Algunos ejemplos muy simples (una clase Leaf y una clase Composite, pero la Composite no implementa recursividad).

# Otros con múltiples métodos, jerarquías confusas o parcialmente correctas pero que rompan el patrón (por ejemplo, el Composite llama métodos de instancias de otras clases pero no mantiene una colección de Component).

# Ejemplos con composiciones anidadas mal hechas (por ejemplo, Composite mantiene una lista de strings en lugar de Component).

# Ejemplos con nombres correctos pero la estructura interna que viola el patrón (por ejemplo, Leaf tiene un add() vacío, Composite hereda mal, Component es usado solo como contenedor de constantes, etc.).

# Asegúrate de que cada ejemplo sea sintácticamente correcto y ejecutable.

# Cada ejemplo debe ser de 10 a 30 líneas máximo.

# Entrega cada ejemplo con un título breve como:

# shell
# Copiar
# Editar
# ### Ejemplo 1: Composite sin recursividad
# seguido del bloque de código correspondiente.

# No expliques el error; solo genera el código.

# No agregues explicaciones fuera de los ejemplos.

# No incluyas comentarios en los ejemplos.

# El objetivo es que estos ejemplos se utilicen para probar detectores de patrones Composite y ver si son capaces de identificar que no son implementaciones válidas del patrón aunque superficialmente se vean como tal.