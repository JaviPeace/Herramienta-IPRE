class MoldeHerramienta:

    def analizar_path(self, path_archivo_o_directorio):
        """
        Analiza un archivo o carpeta, detectando bloques y relaciones de importación.
        Imprime y retorna los patrones detectados.
        """
        bloques = self.obtener_bloques_a_procesar(path_archivo_o_directorio)
        patrones_detectados = []

        for i, bloque in enumerate(bloques, 1):
            print(f"\n🔹 Analizando bloque {i}/{len(bloques)}:")
            for f in bloque:
                print(f" - {f}")

            if len(bloque) == 1:
                archivo = bloque[0]
                print(f"\n--- Análisis de: {archivo} ---")
                res = self.analizar(archivo)
                if res:
                    patrones_detectados.extend(res if isinstance(res, list) else [res])
            else:
                if self.archivos_importan_otros(bloque):
                    import ast
                    trees = []
                    for archivo in bloque:
                        with open(archivo, "r", encoding="utf-8") as f:
                            codigo = f.read()
                        tree = ast.parse(codigo, filename=archivo)
                        trees.extend(tree.body)
                    combined_tree = ast.Module(body=trees, type_ignores=[])
                    res = self.analizar_ast(combined_tree)
                    if res:
                        patrones_detectados.extend(res)
                else:
                    # Analizar cada archivo por separado porque no se importan entre ellos
                    for archivo in bloque:
                        print(f"\n--- Análisis de: {archivo} ---")
                        res = self.analizar(archivo)
                        if res:
                            patrones_detectados.extend(res if isinstance(res, list) else [res])

        return patrones_detectados

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

