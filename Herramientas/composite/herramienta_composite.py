from ast import *
from Moldes.MoldeHerramienta import MoldeHerramienta
from Herramientas.composite.Reglas import reglas_composite
import os
import ast

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
    if os.path.isdir(path_archivo_o_directorio):
        archivos_py = []
        for root, _, files in os.walk(path_archivo_o_directorio):
            for f in files:
                if f.endswith('.py'):
                    archivos_py.append(os.path.join(root, f))
        patrones_detectados = []
        import_relations = {os.path.basename(f): set() for f in archivos_py}
        for archivo in archivos_py:
            herramienta_result = herramienta.analizar(archivo)
            if herramienta_result:
                patrones_detectados.append(archivo)
            # Analizar importaciones
            with open(archivo, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read(), filename=archivo)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ImportFrom):
                        if node.module:
                            mod = node.module.split('.')[-1] + '.py'
                            if mod in import_relations:
                                import_relations[os.path.basename(archivo)].add(mod)
                    elif isinstance(node, ast.Import):
                        for alias in node.names:
                            mod = alias.name.split('.')[-1] + '.py'
                            if mod in import_relations:
                                import_relations[os.path.basename(archivo)].add(mod)
        # Verificar si hay importaciones cruzadas
        hay_imports = any(import_relations[archivo] for archivo in import_relations)
        if patrones_detectados and hay_imports:
            print(f"La carpeta '{os.path.basename(path_archivo_o_directorio)}' cumple con el patrón Composite (hay archivos que se importan entre sí y se detectó el patrón en al menos uno de ellos).")
        else:
            print(f"La carpeta '{os.path.basename(path_archivo_o_directorio)}' NO cumple con el patrón Composite (faltan importaciones cruzadas o no se detectó el patrón en ningún archivo).")
        return patrones_detectados
    else:
        return herramienta.analizar(path_archivo_o_directorio)

