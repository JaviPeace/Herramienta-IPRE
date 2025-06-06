from ast import *
from Moldes.MoldeHerramienta import MoldeHerramienta
from Herramientas.observer.Reglas import reglas_observer

class HerramientaObserver(MoldeHerramienta):
    def __init__(self):
        super().__init__(lambda: reglas_observer)

    def evaluar_patrones(self, resultados, tree):
        patrones = []
        reglas_ok = sum(
            any(
                "no se detectó" not in w.description.lower() and "no se detectaron" not in w.description.lower()
                for w in warnings
            )
            for warnings in resultados
        )
        if reglas_ok >= 2:
            for node in walk(tree):
                if isinstance(node, ClassDef):
                    patrones.append(("Observer", node.lineno))
        return patrones

def analizar(path_archivo):
    HerramientaObserver().analizar(path_archivo)
