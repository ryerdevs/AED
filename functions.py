import random
from clase import *
import pickle
import os

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No existe el archivo", fd, "...")
        print()
        return

    print("Listado de lotes...")
    c = ac = 0
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        r = pickle.load(m)
        c += 1
        ac += r.importe
        print(r)
    m.close()

    p = 0
    if c != 0:
        p = ac / c
    print("Importe promedio de venta:", round(p, 2))
    print()


def generar_archivo(lotes, fd):
    l1 = int(input("Ingrese L1: "))
    l2 = int(input("Ingrese L2: "))
    m = open(fd, "wb")
    for lote in lotes:
        if l1 <= lote.lote <= l2:
            # Guardar solo el lote que cumple la condición
            pickle.dump(lote, m)
    m.close()
    print(f"Archivo '{fd}' generado con éxito.")

def insercion_ordenada(v, lote):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if lote.nombre == v[c].nombre:
            pos = c
            break

        else:
            if lote.nombre < v[c].nombre:
                der = c - 1
            else:
                izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [lote]


def positivo(mensaje):
    while True:
        inicial = int(input(mensaje))
        if inicial > 0:
            return inicial
        print("Ingrese un número mayor a 0")


def cargar():
    n = int(input("Ingrese la Cantidad de Lotes de cargar: "))
    lotes = []
    for i in range(n):
        nombres = ("Juan Cruz", "Joni Bravo", "Johnie Willis", "Bruce Wilis", "Peter Parker", "Spiderman", "Capitan America"
                   ,"Ojo de Halcon", "Viuda Negra", "Angelina Jolie")
        name = random.choice(nombres)
        manzana = random.randint(1, 35)
        lote = random.randint(1,20)
        direction = random.randint(1,4)
        superficie = random.uniform(1000,200000)
        monto = random.uniform(10000, 100000)
        nuevos_lotes = Lote(name, manzana, lote, direction, superficie, monto)
        lotes.append(nuevos_lotes)
    return lotes


def mostrar(lotes):
    n = len(lotes)
    print("Listado de lotes...")
    for i in range(n):
        print(lotes[i])
    print()