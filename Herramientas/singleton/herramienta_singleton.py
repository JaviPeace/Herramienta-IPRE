from ast import *
from Moldes.MoldeHerramienta import MoldeHerramienta
from Herramientas.singleton.Reglas import reglas_singleton

class HerramientaSingleton(MoldeHerramienta):
    def __init__(self):
        super().__init__(lambda: reglas_singleton)

    def evaluar_patrones(self, resultados, tree):
        patrones = []
        reglas_ok = sum(
            any(
                "no se detectó" not in w.description.lower() and "no se detectaron" not in w.description.lower()
                for w in warnings
            )
            for warnings in resultados
        )
        if reglas_ok >= 3 or any(
            any("Decorador Singleton detectado" in w.description for w in warnings)
            for warnings in resultados[4:]
        ):
            for node in walk(tree):
                if isinstance(node, ClassDef):
                    patrones.append(("Singleton", node.lineno))
        return patrones

def analizar(path_archivo):
    HerramientaSingleton().analizar(path_archivo)

