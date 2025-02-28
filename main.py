from functions import *


def main():
    lotes = []
    fd = "lotes.dat"
    op = -1
    while op != 6:
        print("1. Cargar arreglo")
        print("2. Mostrar contenido")
        print("3. Acumulación por manzana y orientación")
        print("4. Generar archivo")
        print("5. Mostrar archivo")
        print("6. Salir")
        op = int(input("Ingrese número de opción: "))

        if op == 1:
            lotes = cargar()

        elif op == 2:
            if lotes:
                mostrar(lotes)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 3:
            if lotes:
                contar(lotes)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 4:
            if lotes:
                generar_archivo(lotes, fd)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 5:
            mostrar_archivo(fd)

        elif op == 6:
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == '__main__':
    main()