from ast import *
from Moldes.MoldeHerramienta import MoldeHerramienta
from Herramientas.decorator.Reglas import reglas_decorator, es_clase_decorator

class HerramientaDecorator(MoldeHerramienta):
    def __init__(self):
        super().__init__(lambda: reglas_decorator)

    def evaluar_patrones(self, resultados, tree):
        patrones = []
        reglas_ok = sum(
            any(
                "no se detectó" not in w.description.lower() and "no se detectaron" not in w.description.lower()
                for w in warnings
            )
            for warnings in resultados
        )
        uso_arroba_warning = None
        for warnings in resultados:
            for w in warnings:
                if ("uso de @" in w.name.lower() or "función" in w.name.lower() or "decorador" in w.name.lower()) and \
                    "no se detectó" not in w.description.lower() and "no se detectaron" not in w.description.lower():
                    uso_arroba_warning = w
            if uso_arroba_warning:
                break

        uso_arroba_ok = uso_arroba_warning is not None

        # Nueva heurística: detectar clases decoradoras clásicas
        es_decorator_clasico = es_clase_decorator(tree)

        # Si solo se cumple la primera regla (misma interfaz) y no las otras, no es patrón
        if len(resultados) > 1 and all(
            any("misma interfaz" in w.name.lower() and "no se detectó" not in w.description.lower() for w in warnings)
            for i, warnings in enumerate(resultados[:1])
        ) and all(
            all("no se detectó" in w.description.lower() or "no se detectaron" in w.description.lower() for w in warnings)
            for warnings in resultados[1:]
        ):
            return patrones

        if reglas_ok >= 1 or uso_arroba_ok or es_decorator_clasico:
            if uso_arroba_ok:
                patrones.append(("Decorator", uso_arroba_warning.lineNumber))
            elif es_decorator_clasico:
                for node in walk(tree):
                    if isinstance(node, ClassDef):
                        patrones.append(("Decorator", node.lineno))
            else:
                for node in walk(tree):
                    if isinstance(node, ClassDef):
                        patrones.append(("Decorator", node.lineno))
        return patrones

def analizar(path_archivo_o_directorio):
    herramienta = HerramientaDecorator()
    bloques = herramienta.obtener_bloques_a_procesar(path_archivo_o_directorio)
    patrones_detectados = []

    for i, bloque in enumerate(bloques, 1):
        print(f"\n🔹 Analizando bloque {i}/{len(bloques)}:")
        for f in bloque:
            print(f" - {f}")

        if len(bloque) == 1:
            archivo = bloque[0]
            print(f"\n--- Análisis de: {archivo} ---")
            res = herramienta.analizar(archivo)
            if res:
                patrones_detectados.extend(res if isinstance(res, list) else [res])
        else:
            if MoldeHerramienta.archivos_importan_otros(bloque):
                trees = []
                import ast
                for archivo in bloque:
                    with open(archivo, "r", encoding="utf-8") as f:
                        codigo = f.read()
                    tree = ast.parse(codigo, filename=archivo)
                    trees.extend(tree.body)
                combined_tree = ast.Module(body=trees, type_ignores=[])
                res = herramienta.analizar_ast(combined_tree)
                if res:
                    patrones_detectados.extend(res)
            else:
                # Analizar cada archivo por separado porque no se importan entre ellos
                for archivo in bloque:
                    print(f"\n--- Análisis de: {archivo} ---")
                    res = herramienta.analizar(archivo)
                    if res:
                        patrones_detectados.extend(res if isinstance(res, list) else [res])

    return patrones_detectados
