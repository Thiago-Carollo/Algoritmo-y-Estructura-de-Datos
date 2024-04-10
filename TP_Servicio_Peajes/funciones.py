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
from clase import *


# ------------------------- VALIDAR PATENTE -----------------------------------
def validar_patente():
    patente = input('Cargue patente: ')
    while not patente.isalnum():
        patente = input('Error. Cargue patente: ')
    return patente


# ------------------------- VALIDAR CODIGO -----------------------------------
def validar_codigo():
    codigo = input('Cargue código de ticket:')
    while not codigo.isdigit() or int(codigo) <= 0:
        codigo = input('ERROR, el código debe ser de caracteres NUMÉRICOS > 0. Cargue código de ticket:')
    return int(codigo)


# ------------------------- VALIDAR VEHICULO ---------------------------------
def validar_vehiculo():
    vehiculo = input('Cargue tipo de vehículo (0:Moto, 1:Auto, 2:Camión):')
    while not vehiculo.isdigit() or int(vehiculo) < 0 or int(vehiculo) > 2:
        vehiculo = input('ERROR, debe cargar un tipo de vehículo (0:Moto, 1:Auto, 2:Camión):')
    return int(vehiculo)


# ------------------------- VALIDAR PAGO -------------------------------------
def validar_pago():
    pago = input('Cargue forma de pago (1:Manual, 2:Telepeaje):')
    while not pago.isdigit() or int(pago) < 1 or int(pago) > 2:
        pago = input('ERROR, cargue forma de pago (1:Manual, 2:Telepeaje):')
    return int(pago)


# ------------------------- VALIDAR CABINA -----------------------------------
def validar_cabina():
    cabina = input('Cargue país de cabina (0:Argentina, 1:Bolivia, 2:Brasil, 3:Paraguay, 4:Uruguay):')
    while not cabina.isdigit() or int(cabina) < 0 or int(cabina) > 4:
        cabina = input('ERROR, cargue país de cabina (0:Argentina, 1:Bolivia, 2:Brasil, 3:Paraguay, 4:Uruguay):')
    return int(cabina)


# ------------------------- VALIDAR KM ---------------------------------------
def validar_km():
    km = input('Cargue kilómetros recorridos (0 para indicar que la cabina actual es la primera que atravesó):')
    while not km.isdigit() or int(km) < 0:
        km = input('ERROR, cargue kilómetros recorridos (0 para indicar que la cabina actual es la primera que atravesó):')
    return int(km)


# ------------------------- AGREGAR BINARIO ---------------------------------------
def add_bin(archivo_binario, new_ticket):
    z = open(archivo_binario, "ab")
    pickle.dump(new_ticket, z)
    z.close()


# ------------------------- MOSTRAR ARCHIVO ---------------------------------------
def mostrar_archivo(archivo_binario):
    if not os.path.exists(archivo_binario):
        return print("EL ARCHIVO NO EXISTE")
    a = open(archivo_binario, "rb")
    size = os.path.getsize(archivo_binario)
    while a.tell() < size:
        r = pickle.load(a)
        print(r,"\n")
    a.close()


# ------------------------- PAIS PATENTE ------------------------------------
def pais_patente(patente):
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    pais_patente = "Otro país"
    n = len(patente)
    if n == 7:
        # ARGENTINA
        if (patente[0] in letras) and (patente[1] in letras) and (patente[2] in numeros) and (patente[3] in numeros) and \
                (patente[4] in numeros) and (patente[5] in letras) and (patente[6] in letras):
            pais_patente = 'Argentina'
        # BRASIL
        elif (patente[0] in letras) and (patente[1] in letras) and (patente[2] in letras) and (
                patente[3] in numeros) and \
                (patente[4] in letras) and (patente[5] in numeros) and (patente[6] in numeros):
            pais_patente = 'Brasil'
        # BOLIVIA
        elif (patente[0] in letras) and (patente[1] in letras) and (patente[2] in numeros) and (
                patente[3] in numeros) and \
                (patente[4] in numeros) and (patente[5] in numeros) and (patente[6] in numeros):
            pais_patente = 'Bolivia'
        # PARAGUAY
        elif (patente[0] in letras) and (patente[1] in letras) and (patente[2] in letras) and (patente[3] in letras) and \
                (patente[4] in numeros) and (patente[5] in numeros) and (patente[6] in numeros):
            pais_patente = 'Paraguay'
        # URUGUAY
        elif (patente[0] in letras) and (patente[1] in letras) and (patente[2] in letras) and (
                patente[3] in numeros) and \
                (patente[4] in numeros) and (patente[5] in numeros) and (patente[6] in numeros):
            pais_patente = 'Uruguay'
    elif n == 6:
        # CHILE
        if (patente[0] in letras) and (patente[1] in letras) and (patente[2] in letras) and \
            (patente[3] in letras) and (patente[4] in numeros) and (patente[5] in numeros):
            pais_patente = 'Chile'
    return pais_patente


# ------------------------- BUSCAR PATENTE ------------------------------------
def buscar_patente(archivo_binario, p):
    if not os.path.exists(archivo_binario):
        return print("EL ARCHIVO NO EXISTE")
    cont = 0
    bin = open(archivo_binario, "rb")
    n = os.path.getsize(archivo_binario)
    while bin.tell() < n:
        registro = pickle.load(bin)
        if registro.patente == p:
            print(registro)
            cont += 1
    bin.close()
    print("Se mostraron : ", cont, " registro/s")


# ------------------------- BUSCAR ARCHIVO ------------------------------------
def buscar_binario(archivo_binario, c):
    if not os.path.exists(archivo_binario):
        return -2
    bin = open(archivo_binario, "rb")
    n = os.path.getsize(archivo_binario)
    while bin.tell() < n:
        dato = pickle.load(bin)
        if dato.cod_ticket == c:
            return dato
    bin.close()
    return -1


# ------------------------- MOSTRAR MATRIZ ------------------------------------
def mostrar_matriz(mc):
    for i in range(len(mc)):
        for j in range(len(mc[0])):
            if mc[i][j] > 0:
                print("Tipo Vehiculo: ", i, "Pais Cabina: ", j, "Son: ", mc[i][j], " vehiculos")


# ------------------------- VEHICULO POR FILA ------------------------------------
def tipo_vehiculo_fila(mc):
    m, n = len(mc), len(mc[0])
    for i in range(m):
        acum = 0
        for j in range(n):
            acum += mc[i][j]
        print("Total de vehiculos por el tipo de vehiculo ", i, ":", acum)


# ------------------------- CABINA COLUMNA ------------------------------------
def tipo_cabina_columna(mc):
    m, n = len(mc), len(mc[0])
    for i in range(n):
        acum = 0
        for j in range(m):
            acum += mc[j][i]
        print("Total de vehiculos por el tipo de cabina ", i, ":", acum)


# ------------------------- CALCULAR PROMEDIO ------------------------------------
def calcular_prom(archivo_binario):
    if not os.path.exists(archivo_binario):
        return -1
    cont = acum = prom = 0
    bin = open(archivo_binario, "rb")
    n = os.path.getsize(archivo_binario)
    while bin.tell() < n:
        registro = pickle.load(bin)
        cont += 1
        acum += registro.km_recorrido
    if cont > 0:
        prom = acum // cont
    bin.close()
    return prom


# ------------------------- SHELL SORT ------------------------------------
def shell_sort(archivo_binario, v, prom):
    if not os.path.exists(archivo_binario):
        return print("EL ARCHIVO NO EXISTE")
    bin = open(archivo_binario, "rb")
    n = os.path.getsize(archivo_binario)
    while bin.tell() < n:
        registro = pickle.load(bin)
        if registro.km_recorrido >= prom:
            v.append(registro)
    # Ordenamiento
    bin.close()
    x = len(v)
    h = 1
    while h <= x // 9:
        h = 3 * h + 1
    while h >0:
        for j in range(h,x):
            y = v[j]
            k = j-h
            while k>= 0 and y.km_recorrido < v[k].km_recorrido:
                v[k+h] = v[k]
                k-=h
            v[k+h]= y
        h //= 3
    return v


# ------------------------- MOSTRAR VECTOR ------------------------------------
def mostrar_vector(v):
    for i in range(len(v)):
        print(v[i])

