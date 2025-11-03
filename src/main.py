# Script de utilidades para automatizar cosas simples mediante Python

# Funcion para Limpiar la Terminal
def limpiarTerminal() -> None:
    import os, platform
    os.system("cls" if platform.system() == "Windows" else "Clear")

# Titulo de Skell's Toys
def mostrarTitulo(titulo: int) -> None:
    match titulo:
        case 0:
            print("-" * 10, end="")
            print(" Skell's Toys ", end="")
            print("-" * 10)
        case _:
            print(f"Titulo No Definido: {titulo}")

# Función Principal
def main() -> None:
    """
    Funcion Principal de Ejecucion"
    """
    # Bucle Infinito Inicial
    opcion1: bool = True
    while opcion1:
        # Limpiar Terminal Primero
        limpiarTerminal()
        # Titulo de Presentacion
        mostrarTitulo(0)
        # Lista de Opciones
        seleccion: int = 0
        print(" 1. Git - GitHub.")
        print(" 2. Red.")
        print(" 3. Salir.")
        # Manejo de Errores
        try:
            seleccion = int(input(" - Seleccion: "))
        except:
            # Opcion Inexistente o Caracter Invalido
            print("Opcion Invalida . . .")
        if seleccion == 3: # Termina la ejecucion del programa
            limpiarTerminal()
            break
        input("Presione una tecla para continuar")

if __name__ == "__main__":
    main()
