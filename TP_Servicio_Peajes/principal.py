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
from clase import *
from funciones import *
# ------------------------- FUNCION PRINCIPAL----------------
def principal():
    band = False
    opcion = -1
    archivo = "peajes-tp4.csv"
    archivo_binario = "archivo-en-binario.dat"
    new_ticket = None
    print('\n\t\t\t\t\t\t\t\t\t\tPEAJES DE SUDAMÉRICA')
    print('*-*-*-' * 17)
    while opcion != 0:
        opcion = mostrar_menu()
        #OPCION 1
        if opcion == 1:
            new_archivo = int(input('Tener en cuenta que si no es la primera vez que crea el archivo binario,'
                                    'el contenido del anterior se eliminará. ¿Desea continuar? '
                                    '0 (para SI) -- 1 (para NO):'))
            if new_archivo == 0:
                crear_archivo_binario(archivo, archivo_binario)
        # OPCION 2
        elif opcion == 2:
            print('Cargue ticket nuevo:')
            codigo_nv = validar_codigo()
            patente_nv = validar_patente()
            vehiculo_nv = validar_vehiculo()
            pago_nv = validar_pago()
            cabina_nv = validar_cabina()
            km_nv = validar_km()
            new_ticket = Ticket(codigo_nv, patente_nv, vehiculo_nv, pago_nv, cabina_nv, km_nv)
            add_bin(archivo_binario, new_ticket)
        # OPCION 3
        elif opcion == 3:
            mostrar_archivo(archivo_binario)
        # OPCION 4
        elif opcion == 4:
            p = validar_patente()
            buscar_patente(archivo_binario, p)

        # OPCION 5
        elif opcion == 5:
            c = validar_codigo()
            pos = buscar_binario(archivo_binario, c)
            if pos == -1:
                print("No se encontro el codigo")
            elif pos == -2:
                print("EL ARCHIVO NO EXISTE")
            else:
                print(pos)

        # OPCION 6
        elif opcion == 6:
            cont_matriz = crear_matriz(archivo_binario)
            if cont_matriz != -1:
                    mostrar_matriz(cont_matriz)
                    band = True
            else:
                print("EL ARCHIVO NO EXISTE")

        # OPCION 7
        elif opcion == 7:
            if band == True:
                tipo_vehiculo_fila(cont_matriz)
                tipo_cabina_columna(cont_matriz)
            else:
                print("Error, primero ingrese opcion 6")

        # OPCION 8
        elif opcion == 8:
            v = []
            prom = calcular_prom(archivo_binario)
            if prom != -1:
                print("La distancia promedio recorrida entre todos los vehiculos es: ", prom)
                h = shell_sort(archivo_binario, v, prom)
                mostrar_vector(h)
            else:
                print("EL ARCHIVO NO EXISTE")

        # OPCION 0
        elif opcion == 0:
            print("\033[35mFin del programa.....\033[0m")
        else:
            print("\033[91mERROR, OPCION INVALIDA.....\033[0m")


if __name__ == '__main__':
    principal()

