

# Imports...
import random
from registro import *


# Generales =======================================================================================================
def validar(limite, mensaje):
    numero = limite
    while numero <= limite:
        numero = int(input(mensaje))
        if numero <= limite:
            print("Error... Ingrese un numero mayor a", limite)
    return numero


def mostrar(arreglo):
    for i in arreglo:
        print(write(i))


def validar_rango(inf, sup, mensaje="Ingrese..."):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Error! El numero debe ser mayor o igual a",
                  inf, " y menor o igual a ", sup)
    return n


def menu():
    cadena = (
        "\n" + "\033[0;37m" + 41 * "=" + "\033[1;33m" + " MENU DE OPCIONES " +
        "\033[0;37m" + "=" * 41 + "\n" +
        "\033[1;36m" + "\n\t1 - Cargar proyectos\n"
        "\t2 - Listar proyectos\n" + "\t3 - Actualizar\n" + "\t4 - Resumen de Lenguajes\n"
        "\t5 - Resumen por Año\n" + "\t6 - Filtrar lenguaje\n" + "\t7 - Productividad\n"
        "\t8 - Salir\n\n" + "\033[0;37m" + "=" * 100 + "\n\nIngrese una opcion:\t")
    return int(input(cadena))


# Punto 1 =======================================================================================================
def cargar(tamano, arreglo, numeros_repetidos, total_pr):
    titulos = ["Catarsismo", "NewTesla", "Resident V", "Hytale", "DataBase",
               "Proteccion", "DarkSouls", "EldenRing", "BitCoin", "GitHub"]
    for i in range(tamano):
        num = ver(numeros_repetidos, total_pr)
        titulo = random.choice(titulos)
        dd = random.randint(1, 30)
        mm = random.randint(1, 12)
        year = random.randint(2000, 2022)
        leng = random.randint(0, 10)
        cant = random.randint(1000, 12000)
        arreglo.append(Proyecto(num, titulo, dd, mm, year, leng, cant))
    return arreglo


# Punto 2 =======================================================================================================
def ordenar_por_titulo(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arreglo[i].titulo > arreglo[j].titulo:
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]


# Punto 3 =======================================================================================================
def actualizar(x, arreglo):
    for i in range(len(arreglo)):
        if arreglo[i].numero == x:
            return i
    return -1


def editar(pos, proyectos):
    print("Se encontro el proyecto: ")
    print(write(proyectos[pos]))
    proyectos[pos].lineas = validar_rango(
        1000, 12000, "\nActualice la cantidad de lineas: ")
    print("\nActualice la fecha\n")
    proyectos[pos].dia = validar_rango(1, 31, "Introduzca Dia:\t")
    proyectos[pos].mes = validar_rango(1, 12, "Introduzca Mes:\t")
    proyectos[pos].anio = validar_rango(2000, 2022, "Introduzca Año:\t")
    print("\nSe ha actualizado correctamente el proyecto.")
    print(write(proyectos[pos]))


# Punto 4 =======================================================================================================
def acumular_por_lenguaje(arreglo):
    v = [0] * 11
    for i in arreglo:
        v[i.lenguaje] += i.lineas
    return v


# Punto 5 =======================================================================================================
def acumular_por_anio(arreglo):
    v = [0] * 23
    for i in arreglo:
        v[i.anio - 2000] += 1
    return v


# Punto 6 =======================================================================================================
def ordenar_por_numero(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arreglo[i].numero > arreglo[j].numero:
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]


def filtrar(ln, arreglo):
    v = []
    for i in range(len(arreglo)):
        if arreglo[i].lenguaje == ln:
            v.append(arreglo[i])
    ordenar_por_numero(v)
    return v


# Punto 7 =======================================================================================================
def buscar_mayor(acumulador):
    mayor = acumulador[0]
    for i in range(1, len(acumulador)):
        if acumulador[i] > mayor:
            mayor = acumulador[i]
    return mayor


def mostrar_mayores(mayor, acumulador):
    for i in range(len(acumulador)):
        if acumulador[i] == mayor:
            print("El año que mas proyecto genero fue: ", i + 2000,
                  " con una cantidad de proyectos de: ", acumulador[i])


# Principal...
def principal():
    opcion = 0
    proyectos = []
    acu_anio = []
    numeros_repetidos = []
    total_pr = 0
    while opcion != 8:
        opcion = menu()

        if opcion == 1:
            print("\n" + 41 * "=" +
                  "\033[1;33m" + " CARGAR PROYECTOS " + "\033[0;37m" + 41 * "=")
            n = validar(
                0, "\nIngrese la cantidad de proyectos a cargar (mayor a 0):\t")
            total_pr += n
            proyectos = cargar(n, proyectos, numeros_repetidos, total_pr)
            input("\nPresione enter para continuar...")

        if len(proyectos) > 0:
            if opcion == 2:
                print(
                    "\n" + 41 * "=" + "\033[1;33m" + " LISTAR PROYECTOS " + "\033[0;37m" + 41 * "=" + "\n")
                ordenar_por_titulo(proyectos)
                mostrar(proyectos)
                input("\nPresione enter para continuar...")

            elif opcion == 3:
                print("\n" + 40 * "=" + " ACTUALIZAR PROYECTOS " + 40 * "=")
                x = int(input("\nIngresar el numero de proyecto a buscar: "))
                pos = actualizar(x, proyectos)
                if pos != -1:
                    editar(pos, proyectos)
                else:
                    print("No se encuentra dicho proyecto!")
                input("\nPresione enter para continuar...")

            elif opcion == 4:
                print(
                    "\n" + 41 * "=" + "\033[1;33m" + " RESUMEN DE LENGUAJES " + "\033[0;37m" + 41 * "=" + "\n")
                acu_lenguaje = acumular_por_lenguaje(proyectos)
                for i in range(len(acu_lenguaje)):
                    if acu_lenguaje[i] > 0:

                        t = (
                            "El lenguaje {:<10} tiene una cantidad de {} lineas")
                        print(t.format(to_string(i), acu_lenguaje[i]))
                input("\nPresione enter para continuar...")

            elif opcion == 5:
                print(
                    "\n" + 41 * "=" + "\033[1;33m" + " RESUMEN POR AÑOS " + "\033[0;37m" + 41 * "=" + "\n")
                acu_anio = acumular_por_anio(proyectos)
                for i in range(len(acu_anio)):
                    if acu_anio[i] > 0:
                        t = ("El año {:<4} tiene una cantidad de {} proyectos")
                        print(t.format(str(i + 2000), acu_anio[i]))
                input("\nPresione enter para continuar...")

            elif opcion == 6:
                print(
                    "\n" + 41 * "=" + "\033[1;33m" + " FILTRAR LENGUAJE " + "\033[0;37m" + 41 * "=" + "\n")
                ln = validar_rango(
                    0, 10, "\nIngrese el numero del lenguaje a filtrar: ")
                filtro = filtrar(ln, proyectos)
                mostrar(filtro)
                input("\nPresione enter para continuar...")

            elif opcion == 7 and len(acu_anio) > 0:
                print(
                    "\n" + 41 * "=" + "\033[1;33m" + " PRODUCTIVIDAD " + "\033[0;37m" + 41 * "=" + "\n")
                mayor = buscar_mayor(acu_anio)
                mostrar_mayores(mayor, acu_anio)
                input("\nPresione enter para continuar...")
            else:
                print("\n" + 35 * "=" +
                      " INGRESE PRIMERO LA OPCION 5 " + 35 * "=")
        else:
            print("\n" + 35 * "=" + " INGRESE PRIMERO LA OPCION 1 " + 35 * "=")
    print("\n" * 50 + 41 * "=" + "\033[1;33m" +
          " SALIR " + "\033[0;37m" + 41 * "=" + "\n")
    print("Gracias por usar nuestros servicios. ¡Vuelva pronto!\n")


if __name__ == "__main__":
    principal()