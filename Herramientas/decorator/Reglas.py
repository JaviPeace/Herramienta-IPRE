from pathlib import Path
import sys
import ast

sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "Molde"))
from Moldes.MoldeRegla import Rule
from Moldes.MoldeWarnings import Warning

class ReglaDecoratorMismaInterfaz(Rule):
    @classmethod
    def name(cls):
        return "Decorator implementa misma interfaz"

    def analyze(self, tree):
        self.warnings = []
        bases = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                bases[node.name] = [base.id for base in node.bases if isinstance(base, ast.Name)]
        # Busca si hay al menos dos clases que comparten una base
        for clase1, base1 in bases.items():
            for clase2, base2 in bases.items():
                if clase1 != clase2 and set(base1) & set(base2):
                    self.warnings.append(Warning(self.name(), 1, f"Decorator '{clase1}' implementa la misma interfaz que '{clase2}' ({', '.join(set(base1) & set(base2))})."))
                    return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó que el decorator implemente la misma interfaz que el componente."))
        return self.warnings

class ReglaDecoratorComposicion(Rule):
    @classmethod
    def name(cls):
        return "Decorator contiene referencia a componente"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                posibles_bases = [base.id for base in node.bases if isinstance(base, ast.Name)]
                for stmt in node.body:
                    if isinstance(stmt, ast.FunctionDef) and stmt.name == "__init__":
                        for assign in stmt.body:
                            if isinstance(assign, ast.Assign):
                                for target in assign.targets:
                                    if isinstance(target, ast.Attribute):
                                        # Busca asignaciones a self.<algo>
                                        if isinstance(assign.value, ast.Name) and assign.value.id in posibles_bases:
                                            self.warnings.append(Warning(self.name(), assign.lineno, f"Clase '{node.name}' contiene referencia a componente '{assign.value.id}'."))
                                            return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó referencia a componente en el decorator."))
        return self.warnings

class ReglaDecoratorDelegacion(Rule):
    @classmethod
    def name(cls):
        return "Llamadas delegadas a la instancia referenciada"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for stmt in node.body:
                    if isinstance(stmt, ast.FunctionDef):
                        for substmt in ast.walk(stmt):
                            if isinstance(substmt, ast.Call) and isinstance(substmt.func, ast.Attribute):
                                if isinstance(substmt.func.value, ast.Attribute) and substmt.func.value.attr != "self":
                                    continue
                                if isinstance(substmt.func.value, ast.Attribute) or (isinstance(substmt.func.value, ast.Name) and substmt.func.value.id == "self"):
                                    self.warnings.append(Warning(self.name(), stmt.lineno, f"Método '{stmt.name}' delega llamada a instancia referenciada en clase '{node.name}'."))
                                    return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectaron llamadas delegadas a la instancia referenciada."))
        return self.warnings

class ReglaDecoratorAnidado(Rule):
    @classmethod
    def name(cls):
        return "Decoradores anidados para funcionalidad acumulativa"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                for stmt in node.body:
                    if isinstance(stmt, ast.FunctionDef) and stmt.name == "__init__":
                        for arg in stmt.args.args[1:]: 
                            if arg.arg.lower() == class_name.lower():
                                self.warnings.append(Warning(self.name(), stmt.lineno, f"Decorador '{class_name}' permite anidamiento para funcionalidad acumulativa."))
                                return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectaron decoradores anidados para funcionalidad acumulativa."))
        return self.warnings

class ReglaUsoArrobaDecorator(Rule):
    @classmethod
    def name(cls):
        return "Uso de @ para aplicar decorador"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.decorator_list:
                for deco in node.decorator_list:
                    if isinstance(deco, ast.Name):
                        self.warnings.append(Warning(self.name(), node.lineno, f"Función '{node.name}' decorada con '@{deco.id}'."))
                        return self.warnings
                    elif isinstance(deco, ast.Call) and isinstance(deco.func, ast.Name):
                        self.warnings.append(Warning(self.name(), node.lineno, f"Función '{node.name}' decorada con '@{deco.func.id}'."))
                        return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó uso de @ para aplicar decorador."))
        return self.warnings

reglas_decorator = [
    ReglaDecoratorMismaInterfaz(),
    ReglaDecoratorComposicion(),
    ReglaDecoratorDelegacion(),
    ReglaDecoratorAnidado(),
    ReglaUsoArrobaDecorator(),
]
