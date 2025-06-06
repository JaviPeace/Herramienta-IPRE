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

    # if not os.path.exists(file_path):
    #     print(f"El archivo '{file_path}' no existe.")
    #     sys.exit(1)

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

    if hasattr(patron_module, "analizar"):
        patron_module.analizar(file_path)
    else:
        print(f"El módulo '{module_path}' no tiene la función 'analizar'.")

if __name__ == "__main__":
    main()
