'''
Algoritmos y Estructura de Datos
Trabajo Practico N°4: Gestión de Cabinas de Peaje
Grupo TP4-G020.
Integrante:
Apellido Y Nombre:      Legajo:     Curso:
Carollo Thiago Lautaro  (94344)     (1K02)
Luis Santiago Ferrera   (400479)    (1K02)
Giménez Sofía Belén     (404824)    (1K02)
Ledesma Lena Sofia      (401269)    (1K02)
'''
# ------------------------- IMPORTS -------------------------
import os
import pickle
from funciones import *
# ------------------------- CREACION DE CLASE -------------------------------
class Ticket:
    def __init__(self, cod_ticket, patente, vehiculo, forma_pago, pais_cabina, km_recorrido):
        self.cod_ticket = cod_ticket
        self.patente = patente
        self.vehiculo = vehiculo
        self.forma_pago = forma_pago
        self.pais_cabina = pais_cabina
        self.km_recorrido = km_recorrido


    def __str__(self):

        return ("| Codigo ticket: " + str(self.cod_ticket)) + (" | Patente: " + self.patente) + (" | Vehiculo: " + str(self.vehiculo)) + (" | Forma de Pago: " + str(self.forma_pago)) + \
            (" | Pais de cabina: " + str(self.pais_cabina)) + (" | KM: " + str(self.km_recorrido)) + (" | País de patente: " + str(pais_patente(self.patente)))


# ------------------------- MENU DE OPCIONES -------------------------------
def mostrar_menu():
    cadena = (
        "\033[0;37m" + 42 * "=" + "\033[1;33m" + " MENU DE OPCIONES " +
        "\033[0;37m" + "=" * 42 + "\n" +
        "\033[1;36m" + "\t1 - Crear archivo binario de registros en base a los datos de los tickets guardados en el archivo de texto dado.\n"
        "\t2 - Cargar por teclado los datos de un ticket y agregar al final del archivo.\n" + "\t3 - Mostrar todos los registros del archivo binario.\n" + "\t4 - Buscar registros por patente cargada por teclado.\n"
        "\t5 - Buscar registro por un código de ticket cargado por teclado.\n" + "\t6 - Cantidad de vehículos de cada combinación posible entre tipo de vehículo y país de cabina.\n" + "\t7 - Cantidad total de vehículos por tipo de vehículo y cantidad total por país de cabina.\n"
        "\t8 - Distancia promedio entre todos los vehículos y arreglo ordenado, de menor a mayor, de los tickets que superen la distancia promedio.\n"+"\t0 - Salir.\n""\033[0;37m" + "=" * 102)
    print(cadena)
    opcion = int(input('Ingrese una opción: '))
    return opcion


# ------------------------- CREAR ARCHIVO BINARIO -------------------------------
def crear_archivo_binario(archivo, archivo_binario):
    if not os.path.exists(archivo):
        return print("EL ARCHIVO NO EXISTE")

    m = open(archivo, "rt")
    bin = open(archivo_binario, "wb")
    m.readline()
    m.readline()
    while True:
        linea = m.readline()
        if not linea.strip():
            break
        if linea[-1] == "\n":
            linea = linea[:-1]
        token = linea.split(",")
        codigo = int(token[0])
        patente = token[1]
        tipo = int(token[2])
        forma_pago = int(token[3])
        cabina = int(token[4])
        kilometros = int(token[5])
        registro = Ticket(codigo, patente, tipo, forma_pago, cabina, kilometros)
        pickle.dump(registro, bin)
    bin.close()
    m.close()


# ------------------------- CREAR MATRIZ ------------------------------------
def crear_matriz(archivo_binario):
    if not os.path.exists(archivo_binario):
        return -1
    bin = open(archivo_binario, "rb")
    n = os.path.getsize(archivo_binario)
    mc = [[0] * 5 for i in range(3)]
    while bin.tell() < n:
        dato = pickle.load(bin)
        mc [dato.vehiculo] [dato.pais_cabina] += 1
    bin.close()
    return mc

