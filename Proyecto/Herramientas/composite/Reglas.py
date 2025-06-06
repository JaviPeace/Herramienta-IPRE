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
        # Busca clases base que sean heredadas por otras clases
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
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for stmt in node.body:
                    # Busca atributos de instancia que sean listas o similares
                    if isinstance(stmt, ast.FunctionDef) and stmt.name == "__init__":
                        for assign in stmt.body:
                            if isinstance(assign, ast.Assign):
                                for target in assign.targets:
                                    if isinstance(target, ast.Attribute) and isinstance(assign.value, (ast.List, ast.Call)):
                                        self.warnings.append(Warning(self.name(), assign.lineno, f"Clase {node.name} contiene colección de hijos."))
                                        return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó colección de componentes hijos en clases compuestas."))
        return self.warnings

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
        # Busca métodos con el mismo nombre en diferentes clases
        metodos_por_clase = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                metodos = set()
                for stmt in node.body:
                    if isinstance(stmt, ast.FunctionDef):
                        metodos.add(stmt.name)
                metodos_por_clase[node.name] = metodos
        # Buscar métodos comunes en al menos dos clases
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
