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

        def tiene_notify_y_update(tree):
            has_notify = False
            has_update = False
            for node in walk(tree):
                if isinstance(node, FunctionDef) and ("notify" in node.name.lower() or "publish" in node.name.lower()):
                    has_notify = True
                if isinstance(node, FunctionDef) and "update" in node.name.lower():
                    has_update = True
            return has_notify and has_update

        if (reglas_ok >= 2 or (found_add_subscriber and found_subscriber_file) or tiene_notify_y_update(tree)):
            for node in walk(tree):
                if isinstance(node, ClassDef):
                    patrones.append(("Observer", node.lineno))
        return patrones

def analizar(path_archivo):
    herramienta = HerramientaObserver()
    herramienta.analizar(path_archivo)
