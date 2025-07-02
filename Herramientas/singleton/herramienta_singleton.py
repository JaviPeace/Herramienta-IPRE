from ast import *
from Moldes.MoldeHerramienta import MoldeHerramienta
from Herramientas.singleton.Reglas import reglas_singleton

class HerramientaSingleton(MoldeHerramienta):
    def __init__(self):
        super().__init__(lambda: reglas_singleton)

    def evaluar_patrones(self, resultados, tree):
        patrones = []
        # Marca como Singleton si alguna regla relevante lo detecta
        for warnings in resultados:
            for w in warnings:
                if (
                    ("singleton" in w.name.lower() or "singleton" in w.description.lower())
                    and ("detectado" in w.description.lower() or "reconocida" in w.description.lower())
                    and ("no se detectó" not in w.description.lower() and "no se detectaron" not in w.description.lower())
                ):
                    patrones.append(("Singleton", w.lineNumber))
        return list(set(patrones))

def analizar(path_archivo_o_directorio):
    herramienta = HerramientaSingleton()
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
 

