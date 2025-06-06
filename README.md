# Herramienta de Detección de Patrones de Diseño

Esta herramienta permite detectar patrones de diseño específicos en archivos de código fuente. Se ejecuta desde la línea de comandos y admite los siguientes patrones: `observer`, `singleton`, `decorator` y `composite`.

## Uso

```bash
python3 main.py <ruta_archivo_o_directorio> <patron>

```

## Resultados tests de la carpeta Tests/

Tests Singleton

| Test   | ¿Debe detectarse Singleton? | Línea esperada (aprox.) |
| ------ | --------------------------- | ----------------------- |
| Test 1 | ✅ Sí                        | 3–6                     |
| Test 2 | ✅ Sí                        | 3–10                    |
| Test 3 | ✅ Sí                        | 3–10                    |
| Test 4 | ❌ No                        | —                       |
| Test 5 | ❌ No                        | —                       |
| Test 6 | ✅ Sí                        | 3–11                    |

Tests Composite

| Test   | ¿Debe detectar Composite? | Línea esperada aprox. |
| ------ | ------------------------- | --------------------- |
| Test 1 | ✅ Sí                      | 3–18                  |
| Test 2 | ✅ Sí                      | 3–18                  |
| Test 3 | ❌ No                      | —                     |
| Test 4 | ❌ No                      | —                     |
| Test 5 | ✅ Sí                      | 3–11                  |


Test Decorator

| Test   | Tipo de Decorator        | ¿Debe detectarse? | Línea clave aproximada |
| ------ | ------------------------ | ----------------- | ---------------------- |
| Test 1 | Clase envolvente         | ✅ Sí              | 3–12                   |
| Test 2 | Decorators anidados      | ✅ Sí              | 3–20                   |
| Test 3 | Decorador funcional      | ✅ Sí              | 3–10                   |
| Test 4 | Herencia normal          | ❌ No              | —                      |
| Test 5 | Wrapper no estándar      | ❌ No              | —                      |
| Test 6 | Funcional con parámetros | ✅ Sí              | 3–13                   |


Test Observer


| Test   | Descripción                     | ¿Debe detectar Observer? | Línea clave aprox. |
| ------ | ------------------------------- | ------------------------ | ------------------ |
| Test 1 | Observer clásico con Subject    | ✅ Sí                     | 3–18               |
| Test 2 | Publisher-Subscriber            | ✅ Sí                     | 3–18               |
| Test 3 | Observadores como funciones     | ✅ Sí                     | 3–13               | 
| Test 4 | Solo almacenamiento de objetos  | ❌ No                     | —                  |
| Test 5 | Delegación directa (sin patrón) | ❌ No                     | —                  |
| Test 6 | Estilo observable reactivo      | ✅ Sí                     | 3–15               |
