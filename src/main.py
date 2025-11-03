# Script de utilidades para automatizar cosas simples mediante Python

import os, platform # Importacion de Librerias

# Funcion para Limpiar la Terminal
def limpiarTerminal() -> None:
    os.system("cls" if platform.system() == "Windows" else "Clear")

# Funcion para Crear el Repositorio
def gitInit(nombre: str) -> None:
    limpiarTerminal()
    mostrarTitulo(1)
    nombre = nombre.replace(" ", "-")
    try:
        os.system(f"git init {nombre}")
    except:
        print("Hubo un error al momento de crear el repositorio")
    else:
        # Creacion del README
        with open(f"{ nombre + '/' if nombre != '' else ''}README.md", "w") as archivo:
            archivo.write(f"# {nombre}")
            archivo.close()
        # Creacion de la LICENCIA
        with open(f"{ nombre + '/' if nombre != '' else ''}LICENSE", "w") as archivo:
            archivo.write(f"# LICENCIA PERSONALIZADA")
            archivo.close()
        # Creacion de Carpetas
        os.system(f"{ 'cd ' + nombre + ' && ' if nombre != '' else ''}mkdir src") # Carpeta de Recursos
        os.system(f"{ 'cd ' + nombre + ' && ' if nombre != '' else ''}mkdir docs") # Carpeta de Documentacion

# Funcion para el manejo de Git mediante Skell's Toys
def gitUI() -> None:
    run: bool = True
    while run:
        limpiarTerminal()
        mostrarTitulo(1)
        seleccion: int = 0
        print(" 1. Crear Repositorio.")
        print(" 2. Comprobar Estado.")
        print(" 3. Realizar Commit.")
        print(" 4. Volver.")
        try:
            seleccion = int(input(" - Seleccion: "))
        except:
            # Opcion Inexistente o Caracter Invalido
            print(" - Opcion Invalida . . .")
            input(" - Presione una tecla para continuar")
        # Manejo de Casos
        match seleccion:
            case 1: # Crear un Repositorio
                gitInit(input(" - Ingrese el nombre del repositorio: "))
            case 2: # Comprobar Estado
                limpiarTerminal()
                mostrarTitulo(1)
            case 3: # Realizar Commit
                limpiarTerminal()
                mostrarTitulo(1)
            case 4: # Volver a Menu Anterior
                limpiarTerminal()
                break
            case _: # Opcion Invalida
                print("Opcion Invalida . . .")
        input(" - Presione ENTER para continuar")

# Titulo de Skell's Toys
def mostrarTitulo(titulo: int) -> None:
    match titulo:
        case 0:
            print("-" * 10, end="")
            print(" Skell's Toys ", end="")
            print("-" * 10)
        case 1:
            print("-" * 10, end="")
            print(" Skell's Toys - Git Tools ", end="")
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
            print(" - Opcion Invalida . . .")
            input(" - Presione una tecla para continuar")
        if seleccion == 3: # Termina la ejecucion del programa
            limpiarTerminal()
            break
        # Procedemos con el manejo de opciones
        limpiarTerminal()
        match seleccion:
            case 1:
                gitUI()
            case _:
                mostrarTitulo(0)
                print(" - Opcion Invalida . . .")
        # input(" - Presione una tecla para continuar")

if __name__ == "__main__":
    main()
