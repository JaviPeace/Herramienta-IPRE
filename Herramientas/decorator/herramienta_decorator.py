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

def analizar(path_archivo):
    HerramientaDecorator().analizar(path_archivo)
