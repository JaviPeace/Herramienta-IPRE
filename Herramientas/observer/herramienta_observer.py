from ast import *
from Moldes.MoldeHerramienta import MoldeHerramienta
from Herramientas.observer.Reglas import reglas_observer, tiene_add_subscriber, existe_archivo_subscriber
import os

class HerramientaObserver(MoldeHerramienta):
    def __init__(self):
        super().__init__(lambda: reglas_observer)

    def evaluar_patrones(self, resultados, tree, path_archivo=None):
        patrones = []
        # PRIMERO: Verifica si hay una lista interna de observadores
        def tiene_lista_observadores(tree):
            for node in walk(tree):
                if isinstance(node, Assign):
                    if isinstance(node.value, (List, Call)):
                        for target in node.targets:
                            if isinstance(target, Attribute) and "observer" in target.attr.lower():
                                return True
            return False

        if not tiene_lista_observadores(tree):
            return patrones

        reglas_ok = sum(
            any(
                "no se detectó" not in w.description.lower() and "no se detectaron" not in w.description.lower()
                for w in warnings
            )
            for warnings in resultados
        )
        found_add_subscriber = tiene_add_subscriber(tree)
        found_subscriber_file = existe_archivo_subscriber(path_archivo) if path_archivo else False
        print(f"Reglas OK: {reglas_ok}, found_add_subscriber: {found_add_subscriber}, found_subscriber_file: {found_subscriber_file}")

        def notify_llama_update(tree):
            # Busca método notify/publish que itere sobre la lista de observadores y llame a update()
            for node in walk(tree):
                if isinstance(node, FunctionDef) and ("notify" in node.name.lower() or "publish" in node.name.lower()):
                    for stmt in node.body:
                        if isinstance(stmt, For):
                            # El iterador debe ser self.observers o observers
                            iter_expr = stmt.iter
                            if (isinstance(iter_expr, Attribute) and "observer" in iter_expr.attr.lower()) or \
                               (isinstance(iter_expr, Name) and "observer" in iter_expr.id.lower()):
                                # Busca llamada a update() sobre el target del for
                                for substmt in stmt.body:
                                    if isinstance(substmt, Expr) and isinstance(substmt.value, Call):
                                        func = substmt.value.func
                                        if isinstance(func, Attribute) and func.attr == "update":
                                            return True
            return False

        if (reglas_ok >= 2 or (found_add_subscriber and found_subscriber_file) or notify_llama_update(tree)):
            for node in walk(tree):
                if isinstance(node, ClassDef):
                    patrones.append(("Observer", node.lineno))
        return patrones

def analizar(path_archivo_o_directorio):
    herramienta = HerramientaObserver()
    bloques = MoldeHerramienta.obtener_bloques_a_procesar(path_archivo_o_directorio)

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