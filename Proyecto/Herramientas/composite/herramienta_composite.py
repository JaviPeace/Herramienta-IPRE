from ast import *
from Moldes.MoldeHerramienta import MoldeHerramienta
from Herramientas.composite.Reglas import reglas_composite

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
        # Aquí puedes agregar detección de otros patrones si lo deseas
        return patrones

def analizar(path_archivo):
    HerramientaComposite().analizar(path_archivo)

