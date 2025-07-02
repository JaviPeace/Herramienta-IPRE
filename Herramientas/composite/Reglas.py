from pathlib import Path
import sys
import ast

sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "Molde"))
from Moldes.MoldeRegla import Rule
from Moldes.MoldeWarnings import Warning

class ReglaClaseComun(Rule):
    @classmethod
    def name(cls):
        return "Clase común para hoja y compuesto"

    def analyze(self, tree):
        self.warnings = []
        bases = set()
        derived = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for base in node.bases:
                    if isinstance(base, ast.Name):
                        bases.add(base.id)
                        derived.add(node.name)
        comunes = bases & derived
        if comunes:
            self.warnings.append(Warning(self.name(), 1, f"Clase común detectada: {', '.join(comunes)}."))
        else:
            self.warnings.append(Warning(self.name(), 1, "No se detectó clase común para hoja y compuesto."))
        return self.warnings

class ReglaCompuestoConColeccion(Rule):
    @classmethod
    def name(cls):
        return "Compuesto contiene colección de hijos"

    def analyze(self, tree):
        self.warnings = []
        tiene_coleccion = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Solo considerar clases que tengan métodos add/remove y una colección
                tiene_add = any(isinstance(stmt, ast.FunctionDef) and stmt.name == "add" for stmt in node.body)
                tiene_remove = any(isinstance(stmt, ast.FunctionDef) and stmt.name == "remove" for stmt in node.body)
                coleccion_detectada = False
                for stmt in node.body:
                    if isinstance(stmt, ast.FunctionDef) and stmt.name == "__init__":
                        for assign in stmt.body:
                            if isinstance(assign, ast.Assign):
                                for target in assign.targets:
                                    if isinstance(target, ast.Attribute) and isinstance(assign.value, ast.List):
                                        if all(isinstance(elt, ast.Str) for elt in assign.value.elts):
                                            self.warnings.append(Warning(self.name(), assign.lineno, f"Clase {node.name} mantiene una lista de strings, no de componentes. Esto rompe la estructura recursiva del patrón Composite."))
                                            return self.warnings
                                        if not self.llama_metodo_polimorfico(node, target.attr):
                                            self.warnings.append(Warning(self.name(), assign.lineno, f"Clase {node.name} contiene una colección pero no itera ni llama métodos polimórficos sobre sus hijos. Esto rompe la uniformidad del patrón Composite."))
                                            return self.warnings
                                        coleccion_detectada = True
                                    elif isinstance(target, ast.Attribute) and isinstance(assign.value, ast.Call):
                                        coleccion_detectada = True
                # Solo marcar como válido si tiene colección y método add/remove
                if coleccion_detectada and (tiene_add or tiene_remove):
                    tiene_coleccion = True
        if not tiene_coleccion:
            self.warnings.append(Warning(self.name(), 1, "No se detectó colección de componentes hijos en clases compuestas. Ninguna clase maneja una colección de hijos junto con métodos add/remove."))
        return self.warnings

    def llama_metodo_polimorfico(self, class_node, collection_name):
        # Busca si hay un método que itere sobre la colección y llame a un método de sus elementos
        for stmt in class_node.body:
            if isinstance(stmt, ast.FunctionDef):
                for substmt in ast.walk(stmt):
                    if isinstance(substmt, ast.For):
                        # for var in self.collection_name
                        if (isinstance(substmt.iter, ast.Attribute)
                            and substmt.iter.attr == collection_name):
                            # Busca llamada a método sobre el iterador
                            for call in ast.walk(substmt):
                                if isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute):
                                    if isinstance(call.func.value, ast.Name) and call.func.value.id == substmt.target.id:
                                        return True
        return False

class ReglaMetodosCompuesto(Rule):
    @classmethod
    def name(cls):
        return "Métodos add/remove/getChild en compuesto"

    def analyze(self, tree):
        self.warnings = []
        metodos = {"add", "remove", "getchild"}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                encontrados = set()
                for stmt in node.body:
                    if isinstance(stmt, ast.FunctionDef) and stmt.name.lower() in metodos:
                        encontrados.add(stmt.name.lower())
                if encontrados:
                    self.warnings.append(Warning(self.name(), node.lineno, f"Clase {node.name} define métodos: {', '.join(encontrados)}."))
                    return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectaron métodos add(), remove() o getChild() en clases compuestas."))
        return self.warnings

class ReglaOperacionPolimorfica(Rule):
    @classmethod
    def name(cls):
        return "Operación polimórfica en hoja y compuesto"

    def analyze(self, tree):
        self.warnings = []
        metodos_por_clase = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                metodos = set()
                for stmt in node.body:
                    if isinstance(stmt, ast.FunctionDef):
                        metodos.add(stmt.name)
                metodos_por_clase[node.name] = metodos
        metodo_comun = set()
        clases = list(metodos_por_clase.keys())
        for i in range(len(clases)):
            for j in range(i+1, len(clases)):
                comunes = metodos_por_clase[clases[i]] & metodos_por_clase[clases[j]]
                metodo_comun |= comunes
        if metodo_comun:
            self.warnings.append(Warning(self.name(), 1, f"Operación polimórfica detectada: {', '.join(metodo_comun)}."))
        else:
            self.warnings.append(Warning(self.name(), 1, "No se detectaron operaciones polimórficas en hoja y compuesto."))
        return self.warnings

reglas_composite = [
    ReglaClaseComun(),
    ReglaCompuestoConColeccion(),
    ReglaMetodosCompuesto(),
    ReglaOperacionPolimorfica(),
]