from ast import *
from Moldes.MoldeHerramienta import MoldeHerramienta
from Herramientas.composite.Reglas import reglas_composite
import os
import ast
from collections import defaultdict, deque

class HerramientaComposite(MoldeHerramienta):
    def __init__(self):
        super().__init__(lambda: reglas_composite)

    def evaluar_patrones(self, resultados, tree):
        patrones = []
        reglas_principales = resultados[:3]
        operacion_polimorfica = resultados[3]
        def es_positiva(w):
            desc = w.description.lower()
            return (
                ("detectada" in desc or "define" in desc or "contiene" in desc)
                and "no se detectó" not in desc and "no se detectaron" not in desc
            )
        reglas_ok = sum(
            any(es_positiva(w) for w in warnings)
            for warnings in reglas_principales
        )
        operacion_ok = any(es_positiva(w) and "operación polimórfica" in w.description.lower() for w in operacion_polimorfica)
        if (reglas_ok >= 1 and operacion_ok) or (reglas_ok >= 2):
            for node in walk(tree):
                if isinstance(node, ClassDef):
                    patrones.append(("Composite", node.lineno))
        return patrones


def analizar(path_archivo_o_directorio):
    herramienta = HerramientaComposite()

    def obtener_bloques_a_procesar(path):
        if os.path.isfile(path):
            return [[path]]
        bloques = []
        bloques_set = set()
        for root, dirs, files in os.walk(path):
            bloque = tuple(sorted(os.path.join(root, f) for f in files if f.endswith('.py')))
            if bloque and bloque not in bloques_set:
                bloques.append(list(bloque))
                bloques_set.add(bloque)
        return bloques

    bloques = obtener_bloques_a_procesar(path_archivo_o_directorio)
    print(f"Analizando carpeta: {path_archivo_o_directorio}")
    print(f"Bloques a procesar: {bloques}")

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
            if archivos_importan_otros(bloque):
                # Analizar bloque combinado
                trees = []
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

def archivos_importan_otros(bloque):
    """Detecta si algún archivo importa a otro archivo del bloque"""
    archivos_nombres = {os.path.splitext(os.path.basename(f))[0] for f in bloque}
    
    for archivo in bloque:
        with open(archivo, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source, filename=archivo)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    # alias.name puede ser modulo sin extension, solo nombre base
                    if alias.name in archivos_nombres:
                        return True
            elif isinstance(node, ast.ImportFrom):
                if node.module is not None:
                    modulo = node.module.split('.')[0]  # solo el primer nivel
                    if modulo in archivos_nombres:
                        return True
    return False