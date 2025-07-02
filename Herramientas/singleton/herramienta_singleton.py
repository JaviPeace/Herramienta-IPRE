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

        # Heurística explícita para Singleton base con __new__ y _instances o variable de clase instance
        def es_singleton_base(node):
            if not isinstance(node, ClassDef):
                return False
            tiene_instances = False
            tiene_new = False
            tiene_instance_var = False
            tiene_control_init = False
            tiene_get_instance = False
            tiene_call = False
            tiene_metaclass_type = False
            for base in node.bases:
                # Detecta metaclase SingletonMeta(type)
                if (isinstance(base, Name) and base.id == "type") or (isinstance(base, Attribute) and base.attr == "type"):
                    tiene_metaclass_type = True
            for stmt in node.body:
                # Busca atributo de clase tipo dict/list llamado _instances o variable instance
                if isinstance(stmt, Assign):
                    for target in stmt.targets:
                        if isinstance(target, Name):
                            if "instance" in target.id.lower():
                                tiene_instance_var = True
                                # Puede ser None, self, o dict/list
                                if isinstance(stmt.value, (Dict, List, Call)):
                                    tiene_instances = True
                                if isinstance(stmt.value, Constant) and stmt.value.value is None:
                                    tiene_instances = True
                # Busca método __new__
                if isinstance(stmt, FunctionDef) and stmt.name == "__new__":
                    for sub in walk(stmt):
                        if isinstance(sub, Attribute) and "instance" in sub.attr.lower():
                            tiene_new = True
                # Busca método __call__ en metaclase
                if isinstance(stmt, FunctionDef) and stmt.name == "__call__":
                    # Debe usar _instances y almacenar la instancia
                    for sub in walk(stmt):
                        if isinstance(sub, Attribute) and "instance" in sub.attr.lower():
                            tiene_call = True
                # Busca método __init__ que controle unicidad
                if isinstance(stmt, FunctionDef) and stmt.name == "__init__":
                    for sub in walk(stmt):
                        if isinstance(sub, If):
                            for testnode in walk(sub.test):
                                if isinstance(testnode, Attribute) and "instance" in testnode.attr.lower():
                                    tiene_control_init = True
                        for assign in walk(stmt):
                            if isinstance(assign, Assign):
                                for t in assign.targets:
                                    if isinstance(t, Attribute) and "instance" in t.attr.lower():
                                        tiene_control_init = True
                # Busca método de clase get_instance
                if isinstance(stmt, FunctionDef) and "get_instance" in stmt.name.lower():
                    tiene_get_instance = True
            # Detecta patrón tipo test 2
            if tiene_instance_var and (tiene_control_init or tiene_get_instance):
                return True
            # Detecta patrón tipo test 8
            if tiene_instances and tiene_new:
                return True
            # Detecta patrón tipo metaclase Singleton (como RefactoringGuru)
            if tiene_metaclass_type and tiene_instances and tiene_call:
                return True
            return False

        # Detecta subclases que heredan de la base Singleton
        def subclases_de_singleton(tree, bases_singleton):
            subclases = []
            for node in walk(tree):
                if isinstance(node, ClassDef):
                    for base in node.bases:
                        if (isinstance(base, Name) and base.id in bases_singleton) or \
                           (isinstance(base, Attribute) and base.attr in bases_singleton):
                            subclases.append(node)
            return subclases

        # Aplica heurística base
        bases_singleton = []
        for node in walk(tree):
            if isinstance(node, ClassDef) and es_singleton_base(node):
                patrones.append(("Singleton", node.lineno))
                bases_singleton.append(node.name)

        # Marca subclases
        for sub in subclases_de_singleton(tree, bases_singleton):
            patrones.append(("Singleton", sub.lineno))

        # Mantiene heurística previa por si acaso
        if reglas_ok >= 3 or any(
            any("Decorador Singleton detectado" in w.description for w in warnings)
            for warnings in resultados[4:]
        ):
            for node in walk(tree):
                if isinstance(node, ClassDef):
                    patrones.append(("Singleton", node.lineno))
        return list(set(patrones))

def analizar(path_archivo_o_directorio):
    herramienta = HerramientaSingleton()
    return herramienta.analizar_path(path_archivo_o_directorio)
 

