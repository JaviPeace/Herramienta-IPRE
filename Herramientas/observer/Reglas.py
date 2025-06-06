from pathlib import Path
import sys
import ast

sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "Molde"))
from Moldes.MoldeRegla import Rule
from Moldes.MoldeWarnings import Warning

class ReglaSubjectMetodos(Rule):
    @classmethod
    def name(cls):
        return "Subject con métodos attach/detach/notify"

    def analyze(self, tree):
        self.warnings = []
        metodos = {"attach", "detach", "notify"}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                encontrados = set()
                for stmt in node.body:
                    if isinstance(stmt, ast.FunctionDef) and stmt.name.lower() in metodos:
                        encontrados.add(stmt.name.lower())
                if encontrados:
                    self.warnings.append(Warning(self.name(), node.lineno, f"Clase '{node.name}' define métodos: {', '.join(encontrados)}."))
                    return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectaron métodos attach(), detach() o notify() en Subject."))
        return self.warnings

class ReglaListaObservadores(Rule):
    @classmethod
    def name(cls):
        return "Lista interna de observadores"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for stmt in node.body:
                    if isinstance(stmt, ast.FunctionDef) and stmt.name == "__init__":
                        for assign in stmt.body:
                            if isinstance(assign, ast.Assign):
                                for target in assign.targets:
                                    if isinstance(target, ast.Attribute) and (
                                        "observer" in target.attr.lower() or "observers" in target.attr.lower()
                                    ):
                                        self.warnings.append(Warning(self.name(), assign.lineno, f"Clase '{node.name}' contiene lista interna de observadores '{target.attr}'."))
                                        return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó lista interna de observadores."))
        return self.warnings

class ReglaObservadorUpdate(Rule):
    @classmethod
    def name(cls):
        return "Observador implementa update()"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for stmt in node.body:
                    if isinstance(stmt, ast.FunctionDef) and stmt.name == "update":
                        self.warnings.append(Warning(self.name(), stmt.lineno, f"Clase '{node.name}' implementa método update()."))
                        return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó método update() en observadores."))
        return self.warnings

class ReglaNotificacionEnEstado(Rule):
    @classmethod
    def name(cls):
        return "Notificación en métodos que alteran el estado"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for stmt in ast.walk(node):
                    if isinstance(stmt, ast.Call) and (
                        (isinstance(stmt.func, ast.Name) and stmt.func.id == "notify") or
                        (isinstance(stmt.func, ast.Attribute) and stmt.func.attr == "notify")
                    ):
                        self.warnings.append(Warning(self.name(), node.lineno, f"Método '{node.name}' notifica a observadores (llama a notify())."))
                        return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó notificación a observadores en métodos que alteran el estado."))
        return self.warnings

class ReglaFuncionCallbackObserver(Rule):
    @classmethod
    def name(cls):
        return "Uso de callbacks/listeners como observadores"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for stmt in node.body:
                    if isinstance(stmt, ast.FunctionDef) and stmt.name == "__init__":
                        for assign in stmt.body:
                            if isinstance(assign, ast.Assign):
                                for target in assign.targets:
                                    if isinstance(target, ast.Attribute) and (
                                        "observer" in target.attr.lower() or
                                        "observers" in target.attr.lower() or
                                        "listener" in target.attr.lower() or
                                        "listeners" in target.attr.lower() or
                                        "callback" in target.attr.lower() or
                                        "callbacks" in target.attr.lower()
                                    ):
                                        self.warnings.append(Warning(self.name(), assign.lineno, f"Clase '{node.name}' contiene lista de callbacks/observers/listeners '{target.attr}'."))
                                        return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó uso de callbacks/listeners/observers como observadores."))
        return self.warnings

class ReglaNotificacionPorIteracion(Rule):
    @classmethod
    def name(cls):
        return "Notificación por iteración sobre observadores"

    def analyze(self, tree):
        self.warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for stmt in node.body:
                    if isinstance(stmt, ast.For):
                        if isinstance(stmt.iter, ast.Attribute):
                            nombre_lista = stmt.iter.attr.lower()
                            if any(word in nombre_lista for word in ["observer", "observers", "listener", "listeners", "callback", "callbacks"]):
                                for substmt in stmt.body:
                                    if isinstance(substmt, ast.Expr) and isinstance(substmt.value, ast.Call):
                                        self.warnings.append(Warning(self.name(), node.lineno, f"Método '{node.name}' notifica a observadores por iteración sobre '{stmt.iter.attr}'."))
                                        return self.warnings
        self.warnings.append(Warning(self.name(), 1, "No se detectó notificación por iteración sobre observadores."))
        return self.warnings

reglas_observer = [
    ReglaSubjectMetodos(),
    ReglaListaObservadores(),
    ReglaObservadorUpdate(),
    ReglaNotificacionEnEstado(),
    ReglaFuncionCallbackObserver(),
    ReglaNotificacionPorIteracion(),
]
