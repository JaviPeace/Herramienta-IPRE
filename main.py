import sys
import importlib
import os

def main():
    if len(sys.argv) != 3:
        print("Uso: python main.py <path_archivo> <patron>")
        print("Patrones disponibles: Composite, Decorator, Observer, Singleton")
        sys.exit(1)

    file_path = sys.argv[1]
    patron = sys.argv[2].capitalize()

    patrones_validos = ["Composite", "Decorator", "Observer", "Singleton"]
    if patron not in patrones_validos:
        print(f"Patrón '{patron}' no es válido. Opciones: {', '.join(patrones_validos)}")
        sys.exit(1)

    module_path = f"Herramientas.{patron.lower()}.herramienta_{patron.lower()}"

    try:
        patron_module = importlib.import_module(module_path)
    except ModuleNotFoundError as e:
        print(f"No se encontró el módulo '{module_path}': {e}")
        sys.exit(1)

    if not hasattr(patron_module, "analizar"):
        print(f"El módulo '{module_path}' no tiene la función 'analizar'.")
        sys.exit(1)

    if os.path.isdir(file_path):
        for root, _, files in os.walk(file_path):
            for fname in files:
                if fname.endswith(".py"):
                    fpath = os.path.join(root, fname)
                    print(f"\nAnalizando archivo: {fpath}")
                    patron_module.analizar(fpath)
    else:
        patron_module.analizar(file_path)

if __name__ == "__main__":
    main()
