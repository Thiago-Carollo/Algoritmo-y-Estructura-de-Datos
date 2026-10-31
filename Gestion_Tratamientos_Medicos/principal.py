from afiliado import Afiliado
from tratamiento import Tratamiento


def mostrar_menu():
    cadena = (
            "\033[0;37m" + 42 * "=" + "\033[1;33m" + " MENU DE OPCIONES " +
            "\033[0;37m" + "=" * 42 + "\n" +
            "\033[1;36m" + "\t1. Cargar afiliados\n" +
            "\t2. Cargar tratamientos\n" +
            "\t3. Mostrar resultados (r3.1 a r3.7)\n" +
            "\t4. Listar DNIs de pacientes disponibles\n" +
            "\t5. Buscar tratamientos por DNI (Teclado)\n" +
            "\t0. Salir\n" +
            "\033[0;37m" + "=" * 102
    )
    print(cadena)


def leer_opcion():
    texto = input("Ingrese opción: ")
    if texto.strip().isdigit():
        return int(texto)
    return -1


def insertar_ordenado_afiliado(vector, afiliado):
    izq = 0
    der = len(vector) - 1
    pos = len(vector)

    while izq <= der:
        c = (izq + der) // 2
        if vector[c].dni == afiliado.dni:
            pos = c
            break
        if afiliado.dni < vector[c].dni:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq

    vector.append(None)
    for i in range(len(vector) - 1, pos, -1):
        vector[i] = vector[i - 1]
    vector[pos] = afiliado


def crear_afiliado_desde_linea(linea):
    campos = linea.split(",")
    dni = int(campos[0])
    cod_obra_social = int(campos[1])
    nivel_cobertura = int(campos[2])
    tope = float(campos[3])
    return Afiliado(dni, cod_obra_social, nivel_cobertura, tope)


def cargar_afiliados():
    vector = []
    archivo = open("coberturas.csv", "r", encoding="utf-8")
    archivo.readline()
    for linea in archivo:
        linea = linea.strip()
        if linea == "":
            continue
        afiliado = crear_afiliado_desde_linea(linea)
        insertar_ordenado_afiliado(vector, afiliado)
    archivo.close()
    return vector


def crear_tratamiento_desde_linea(linea):
    campos = linea.split(",")
    dni = int(campos[0])
    nombre = campos[1]
    apellido = campos[2]
    icd10 = campos[3]
    monto_base = float(campos[4])
    complejidad = campos[5]
    id_algoritmo = int(campos[6])
    return Tratamiento(dni, nombre, apellido, icd10, monto_base,
                       complejidad, id_algoritmo)


def cargar_tratamientos():
    vector = []
    archivo = open("tratamientos.csv", "r", encoding="utf-8")
    archivo.readline()
    for linea in archivo:
        linea = linea.strip()
        if linea == "":
            continue
        vector.append(crear_tratamiento_desde_linea(linea))
    archivo.close()
    return vector


def buscar_afiliado_binaria(v_afiliados, dni):
    izq = 0
    der = len(v_afiliados) - 1
    while izq <= der:
        c = (izq + der) // 2
        if v_afiliados[c].dni == dni:
            return v_afiliados[c]
        if dni < v_afiliados[c].dni:
            der = c - 1
        else:
            izq = c + 1
    return None


def obtener_porcentaje_cobertura(nivel, complejidad):
    if nivel == 1:
        return 0.50 if complejidad == "R" else 0.40
    elif nivel == 2:
        return 0.70 if complejidad == "R" else 0.60
    elif nivel == 3:
        return 0.90 if complejidad == "R" else 0.80
    return 0.0


def mostrar_resultados_opcion_3(v_afiliados, v_tratamientos):
    monto_total_cubierto = 0.0
    monto_total_no_cubierto = 0.0
    cant_tope_aplicado = 0
    cant_no_afiliados = 0
    acum_obras_sociales = [0.0] * 20
    mayor_monto_no_cubierto = -1.0
    dni_mayor_no_cubierto = None

    for t in v_tratamientos:
        afiliado = buscar_afiliado_binaria(v_afiliados, t.dni)

        if afiliado is None:
            cant_no_afiliados += 1
            monto_cubierto = 0.0
            monto_no_cubierto = t.monto_final
        else:
            porcentaje = obtener_porcentaje_cobertura(afiliado.nivel_cobertura, t.complejidad)
            monto_cubierto = t.monto_final * porcentaje

            if monto_cubierto > afiliado.tope:
                monto_cubierto = afiliado.tope
                cant_tope_aplicado += 1

            monto_no_cubierto = t.monto_final - monto_cubierto

            idx_os = afiliado.cod_obra_social - 1
            acum_obras_sociales[idx_os] += monto_cubierto

        monto_total_cubierto += monto_cubierto
        monto_total_no_cubierto += monto_no_cubierto

        if monto_no_cubierto > mayor_monto_no_cubierto:
            mayor_monto_no_cubierto = monto_no_cubierto
            dni_mayor_no_cubierto = t.dni

    cod_os_mayor = 1
    for i in range(1, 20):
        if acum_obras_sociales[i] > acum_obras_sociales[cod_os_mayor - 1]:
            cod_os_mayor = i + 1

    print("r3.1:", round(monto_total_cubierto, 2))
    print("r3.2:", round(monto_total_no_cubierto, 2))
    print("r3.3:", cant_tope_aplicado)
    print("r3.4:", cant_no_afiliados)
    print("r3.5:", cod_os_mayor)
    print("r3.6:", dni_mayor_no_cubierto)

    porcentaje_no_afiliados = (cant_no_afiliados * 100) / len(v_tratamientos)
    print("r3.7:", round(porcentaje_no_afiliados, 2))


def listar_pacientes_disponibles(v_tratamientos):
    # Genera una lista de DNIs únicos sin usar sets ni diccionarios (regla TP4)
    dnis_unicos = []
    for t in v_tratamientos:
        encontrado = False
        for dni in dnis_unicos:
            if dni == t.dni:
                encontrado = True
                break
        if not encontrado:
            dnis_unicos.append(t.dni)

    print(f"\n\033[1;33m--- Lista de Pacientes ({len(dnis_unicos)} DNI únicos en total) ---\033[0m")
    for dni in dnis_unicos:
        print(f"- DNI: {dni}")
    print("\033[0;37m---------------------------------------------------\033[0m")


def buscar_tratamientos_por_dni(v_afiliados, v_tratamientos):
    dni_buscar = input("\033[0;37mIngrese el DNI del paciente a buscar: ")
    while not dni_buscar.isdigit():
        dni_buscar = input("\033[91mError. Ingrese un DNI válido (solo números): \033[0;37m")

    dni_buscar = int(dni_buscar)
    cont_encontrados = 0

    print(f"\n\033[1;33m--- Resultados para el DNI {dni_buscar} ---\033[0m")

    # Verificamos si el paciente está afiliado usando la búsqueda binaria
    afiliado = buscar_afiliado_binaria(v_afiliados, dni_buscar)
    if afiliado is not None:
        print(
            f"\033[1;32mEstado: PACIENTE AFILIADO (Obra Social: {afiliado.cod_obra_social}, Nivel: {afiliado.nivel_cobertura})\033[0m")
    else:
        print(f"\033[1;31mEstado: PACIENTE NO AFILIADO\033[0m")

    print("\033[1;33mTratamientos registrados:\033[0m")
    for t in v_tratamientos:
        if t.dni == dni_buscar:
            print(t)
            cont_encontrados += 1

    if cont_encontrados == 0:
        print("\033[91mNo se encontraron tratamientos para el DNI ingresado.\033[0m")
    else:
        print(f"\033[1;36mTotal de tratamientos encontrados: {cont_encontrados}\033[0m")
    print("\033[0;37m---------------------------------------------------\033[0m")


def main():
    v_afiliados = []
    v_tratamientos = []
    afiliados_cargados = False
    tratamientos_cargados = False
    opcion = -1

    print('\n\t\t\t\t\t\tSISTEMA DE GESTIÓN DE TRATAMIENTOS MÉDICOS')
    print('*-*-*-' * 17)

    while opcion != 0:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            v_afiliados = cargar_afiliados()
            afiliados_cargados = True
            print("\033[1;36m-> Afiliados cargados correctamente.\033[0m")
        elif opcion == 2:
            v_tratamientos = cargar_tratamientos()
            tratamientos_cargados = True
            print("\033[1;36m-> Tratamientos cargados correctamente.\033[0m")
        elif opcion == 3:
            if afiliados_cargados and tratamientos_cargados:
                mostrar_resultados_opcion_3(v_afiliados, v_tratamientos)
            else:
                print("\033[91mError: Debe cargar los afiliados y tratamientos primero.\033[0m")
        elif opcion == 4:
            if tratamientos_cargados:
                listar_pacientes_disponibles(v_tratamientos)
            else:
                print("\033[91mError: Debe cargar los tratamientos primero.\033[0m")
        elif opcion == 5:
            if afiliados_cargados and tratamientos_cargados:
                buscar_tratamientos_por_dni(v_afiliados, v_tratamientos)
            else:
                print("\033[91mError: Debe cargar los afiliados y tratamientos primero.\033[0m")
        elif opcion == 0:
            pass
        else:
            print("\033[91mERROR, OPCION INVALIDA.....\033[0m")


if __name__ == "__main__":
    main()