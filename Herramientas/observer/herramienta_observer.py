from ast import *
from Moldes.MoldeHerramienta import MoldeHerramienta
from Herramientas.observer.Reglas import reglas_observer, tiene_add_subscriber, existe_archivo_subscriber
import os

class HerramientaObserver(MoldeHerramienta):
    def __init__(self):
        super().__init__(lambda: reglas_observer)

    def evaluar_patrones(self, resultados, tree, path_archivo=None):
        patrones = []
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

        # Si se cumplen las condiciones, marcar patrón Observer
        if (reglas_ok >= 2 or (found_add_subscriber and found_subscriber_file)):
            for node in walk(tree):
                if isinstance(node, ClassDef):
                    patrones.append(("Observer", node.lineno))
        return patrones

def analizar(path_archivo):
    herramienta = HerramientaObserver()
    herramienta.analizar(path_archivo)
