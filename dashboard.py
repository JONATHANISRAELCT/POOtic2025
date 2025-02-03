import os
import colorama
from colorama import Fore, Style

def mostrar_codigo(ruta_script):
    """Muestra el contenido de un archivo de script."""
    if not os.path.exists(ruta_script):
        print(Fore.RED + "El archivo no se encontró." + Style.RESET_ALL)
        return
    
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print(Fore.CYAN + f"\n--- Código de {ruta_script} ---\n" + Style.RESET_ALL)
            print(archivo.read())
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error al leer el archivo: {e}" + Style.RESET_ALL)

def cargar_scripts(directorio_base):
    """Carga dinámicamente todos los scripts dentro del directorio_base."""
    opciones = {}
    contador = 1
    
    for raiz, _, archivos in os.walk(directorio_base):
        for archivo in archivos:
            if archivo.endswith(".py"):
                ruta_relativa = os.path.relpath(os.path.join(raiz, archivo), directorio_base)
                opciones[str(contador)] = ruta_relativa
                contador += 1
    
    return opciones

def mostrar_menu():
    """Muestra el menú y permite seleccionar un script para ver su código."""
    colorama.init()
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    opciones = cargar_scripts(ruta_base)
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
        print(Fore.YELLOW + "\n******** Menu Principal - Dashboard *************" + Style.RESET_ALL)
        
        if not opciones:
            print(Fore.RED + "No se encontraron scripts en la carpeta." + Style.RESET_ALL)
            break
        
        for key, ruta in opciones.items():
            print(Fore.GREEN + f"{key} - {ruta}" + Style.RESET_ALL)
        print(Fore.RED + "0 - Salir" + Style.RESET_ALL)
        
        eleccion = input(Fore.BLUE + "\nElige un script para ver su código o '0' para salir: " + Style.RESET_ALL)
        
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
            input(Fore.BLUE + "\nPresiona Enter para continuar..." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Opción no válida. Intenta de nuevo." + Style.RESET_ALL)
            input(Fore.BLUE + "\nPresiona Enter para continuar..." + Style.RESET_ALL)

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()