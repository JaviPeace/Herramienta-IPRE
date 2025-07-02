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


## Resultados testing Hito_4/

Para testear se hicieron 30 tests con el patrón incluido y 30 tests sin el patrón para cada patrón

| Patrón    | VP/30 | FP/30 | FN | Precisión | Recall | F1-score |
| --------- | ----- | ----- | -- | --------- | ------ | -------- |
| Composite | 30    | 8     | 0  | 78.9%     | 100%   | 88.2%    |
| Decorator | 28    | 0     | 2  | 100%      | 93.3%  | 96.5%    |
| Singleton | 30    | 0     | 0  | 100.0%    | 100%   | 100%     |
| Observer  | 24    | 10    | 6  | 70.6%     | 80.0%  | 75.0%    |

En conclusión:
🔹 Decorator logra resultados excelentes (Precisión 100%, F1 96.5%), demostrando un detector sólido. Esta herramienta falló en los dos test que tenían varios archivos. 
🔹 Composite mejora notablemente (F1 88.2%) gracias a menor FP.
🔹 Singleton mantiene recall perfecto, pero precisión baja (50%), indicando muchos falsos positivos.
🔹 Observer mantiene buen balance (F1 75%) con recall alto y precisión razonable. Esta fue la herramienta que tuvo menor rendimiento lo que se puede deber a la complejidad del patrón en relación a los otros.

Los test respectivos que fueron errados por patrón fueron los siguientes

Composite/Tests_falsos_positivos
- Test_3_Leaf_con_método_add_vacío
- Test_8_Composite_con_lista_de_enteros
- Test_10_Composite_con_hijos_pero_no_Component
- Test_16_Composite_que_solo_tiene_add
- Test_21_Leaf_con_método_add
- Test_24_Composite_con_lista_de_números
- Test_27_Composite_sin_método_principal
- Test_29_Composite_que_solo_agrega_int

Decorator/Tests_positivos
- Test_6_Decorador_de_notificaciones
- Test_25_Decorador_modular_distribuido_en_archivos

Observer/Tests_positivos
- Test_Detallado_VehicleRouting (en particular este test la herramienta no fue capaz de leer bien este archivo)
- Test_3_Observadores_con_nombres
- Test_4_Observadores_condicionales
- Test_5_Múltiples_tipos_de_eventos
- Test_11_Observer_con_parámetro_en_update
- Test_RefactoringGuru

Observer/Tests_falsos_positivos
- Test_5_notify()_no_llama_update()
- Test_7_Subject_con_lista_pero_sin_notify
- Test_8_attach_agrega_None
- Test_9_notify()_llama_print
- Test_11_Subject_usa_lista_de_strings
- Test_12_Subject_con_atributo_pero_sin_lógica
- Test_16_attach_no_agrega_nada
- Test_22_Subject_con_lista_vacía_y_notify_sin_llamadas
- Test_29_Subject_con_notify_sin_llamadas
- Test_30_notify()_con_conteo_sin_update


