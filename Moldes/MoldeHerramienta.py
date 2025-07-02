class MoldeHerramienta:

    @staticmethod
    def obtener_bloques_a_procesar(path):
        import os
        if os.path.isfile(path):
            return [[path]]
        bloques = []
        bloques_set = set()
        for root, dirs, files in os.walk(path):
            bloque = tuple(sorted(os.path.join(root, f) for f in files if f.endswith('.py')))
            if bloque and bloque not in bloques_set:
                bloques.append(list(bloque))
                bloques_set.add(bloque)
        return bloques

    @staticmethod
    def archivos_importan_otros(bloque):
        import os, ast
        archivos_nombres = {os.path.splitext(os.path.basename(f))[0] for f in bloque}
        for archivo in bloque:
            with open(archivo, "r", encoding="utf-8") as f:
                source = f.read()
            tree = ast.parse(source, filename=archivo)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name in archivos_nombres:
                            return True
                elif isinstance(node, ast.ImportFrom):
                    if node.module is not None:
                        modulo = node.module.split('.')[0]
                        if modulo in archivos_nombres:
                            return True
        return False
    def __init__(self, reglas_factory):
        self.reglas_factory = reglas_factory

    def analizar(self, path_archivo):
        import os
        from ast import parse, walk, ClassDef

        if not os.path.exists(path_archivo):
            print("Este path no existe")
            return

        with open(path_archivo, "r", encoding="utf-8") as f:
            source = f.read()
        tree = parse(source)

        return self.analizar_ast(tree)

    def analizar_ast(self, tree):
        reglas = self.reglas_factory()

        if len(reglas) == 0:
            print("No hay reglas definidas para el patrón.")
            return

        resultados = []
        for regla in reglas:
            warnings = regla.analyze(tree)
            resultados.append(warnings)
            for warning in warnings:
                print(str(warning))

        patrones_detectados = self.evaluar_patrones(resultados, tree)
        if patrones_detectados:
            for patron, linea in patrones_detectados:
                print(f"Patrón {patron} detectado en la línea {linea}")
            return patrones_detectados
        else:
            print("No se detectó el patrón.")
            return []

    def evaluar_patrones(self, resultados, tree):
        raise NotImplementedError("Debe implementar evaluar_patrones en la herramienta concreta.")

