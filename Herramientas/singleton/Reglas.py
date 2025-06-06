from pathlib import Path
import sys
import ast

sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "Molde"))
from Moldes.MoldeRegla import Rule
from Moldes.MoldeWarnings import Warning

class ReglaConstructorPrivado(Rule):
    @classmethod
    def name(cls):
        return "Constructor privado o control de instancia"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "__new__":
                for stmt in node.body:
                    if isinstance(stmt, ast.If):
                        for substmt in stmt.body:
                            if isinstance(substmt, ast.Assign):
                                for target in substmt.targets:
                                    if isinstance(target, ast.Attribute) and target.attr == "_instance":
                                        self.warnings.append(Warning(self.name(), node.lineno, "Control de instancia en __new__ detectado."))
                                        return self.warnings
            if isinstance(node, ast.FunctionDef) and node.name == "__init__":
                for stmt in node.body:
                    if isinstance(stmt, ast.Raise):
                        self.warnings.append(Warning(self.name(), node.lineno, "Constructor privado detectado (raise en __init__)."))
                        return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó constructor privado ni control de instancia en __new__."))
        return self.warnings

class ReglaAtributoEstatico(Rule):
    @classmethod
    def name(cls):
        return "Atributo estático de instancia Singleton"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for stmt in node.body:
                    if isinstance(stmt, ast.Assign):
                        for target in stmt.targets:
                            if isinstance(target, ast.Name) and "_instance" in target.id:
                                self.warnings.append(Warning(self.name(), stmt.lineno, f"Atributo estático '{target.id}' detectado en clase '{node.name}'."))
                                return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó atributo estático de instancia Singleton (ej: _instance)."))
        return self.warnings

class ReglaMetodoEstaticoAcceso(Rule):
    @classmethod
    def name(cls):
        return "Método de acceso a instancia Singleton"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.name == "__new__":
                    self.warnings.append(Warning(self.name(), node.lineno, "Método especial __new__ detectado."))
                    return self.warnings
                if node.name.lower() in ["getinstance", "instance"]:
                    self.warnings.append(Warning(self.name(), node.lineno, f"Método de acceso '{node.name}' detectado."))
                    return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó método de acceso a la instancia Singleton (ej: __new__, getInstance)."))
        return self.warnings

class ReglaNoMultiplesInstancias(Rule):
    @classmethod
    def name(cls):
        return "No múltiples instanciaciones"

    def analyze(self, tree):
        self.warnings = []
        clases = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                clases.add(node.name)
        instancias = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id in clases:
                    instancias[node.func.id] = instancias.get(node.func.id, 0) + 1
                if isinstance(node.func, ast.Attribute) and node.func.attr == "__new__":
                    instancias["__new__"] = instancias.get("__new__", 0) + 1
        if all(count == 1 for count in instancias.values()) or "__new__" in instancias:
            self.warnings.append(Warning(self.name(), 1, "No se detectaron múltiples instanciaciones visibles."))
            return self.warnings
        for clase, count in instancias.items():
            if count > 1:
                self.warnings.append(Warning(self.name(), 1, f"Se detectaron múltiples instanciaciones de '{clase}'."))
                return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectaron múltiples instanciaciones visibles."))
        return self.warnings

class ReglaDecoradorSingleton(Rule):
    @classmethod
    def name(cls):
        return "Decorador Singleton"

    def analyze(self, tree):
        self.warnings = []
        singleton_decorator_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "singleton":
                singleton_decorator_found = True
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for deco in node.decorator_list:
                    if isinstance(deco, ast.Name) and deco.id == "singleton":
                        if singleton_decorator_found:
                            self.warnings.append(Warning(self.name(), node.lineno, f"Decorador Singleton detectado en clase '{node.name}'."))
                            return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó decorador Singleton."))
        return self.warnings

reglas_singleton = [
    ReglaConstructorPrivado(),
    ReglaAtributoEstatico(),
    ReglaMetodoEstaticoAcceso(),
    ReglaNoMultiplesInstancias(),
    ReglaDecoradorSingleton(),
]
