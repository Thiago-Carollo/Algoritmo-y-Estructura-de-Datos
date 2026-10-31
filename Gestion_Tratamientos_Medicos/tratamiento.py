class Tratamiento:
    def __init__(self, dni, nombre, apellido, icd10, monto_base,
                 complejidad, id_algoritmo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.icd10 = icd10
        self.monto_base = monto_base
        self.complejidad = complejidad
        self.id_algoritmo = id_algoritmo
        self.monto_final = calcular_monto_final(id_algoritmo, icd10,
                                                complejidad, monto_base)

    def es_alta_complejidad(self):
        return self.complejidad == "A"

    def letra_icd(self):
        return obtener_letra(self.icd10)

    def __str__(self):
        return ("DNI: " + str(self.dni) + " | " + self.nombre + " " +
                self.apellido + " | ICD10: " + self.icd10 +
                " | Base: " + str(self.monto_base) +
                " | Complejidad: " + self.complejidad +
                " | Algoritmo: " + str(self.id_algoritmo) +
                " | Final: " + str(round(self.monto_final, 2)))


# ---------------------------------------------------------------
# Funciones auxiliares para interpretar el código ICD10 (ej: "B83.5")
# ---------------------------------------------------------------
def obtener_letra(icd10):
    return icd10[0].upper()


def obtener_bloque(icd10):
    # Número entre la letra y el punto: "B83.5" -> 83
    partes = icd10.split(".")
    return int(partes[0][1:])


def obtener_decimal(icd10):
    # Número a la derecha del punto: "B83.5" -> 5
    partes = icd10.split(".")
    if len(partes) < 2 or partes[1] == "":
        return 0
    return int(partes[1])


# ---------------------------------------------------------------
# CÁLCULO NORMAL (reglas del TP1)
# ---------------------------------------------------------------
ADICIONAL_A_L = 25000
ADICIONAL_M_Z = 40000
ADICIONAL_U = 100000
RECARGO_ALTA_COMPLEJIDAD = 0.05


def calcular_adicional_letra(icd10):
    letra = obtener_letra(icd10)
    if letra == "U":
        return ADICIONAL_U
    elif letra <= "L":
        return ADICIONAL_A_L
    else:
        return ADICIONAL_M_Z


def calcular_porcentaje_normal(icd10, complejidad, monto_base,
                               factor_decimal=1):
    subtotal = monto_base + calcular_adicional_letra(icd10)
    porcentaje = obtener_decimal(icd10) * factor_decimal
    return subtotal * porcentaje / 100


def calculo_normal(icd10, complejidad, monto_base):
    subtotal = monto_base + calcular_adicional_letra(icd10)
    monto_final = subtotal + calcular_porcentaje_normal(icd10, complejidad,
                                                        monto_base)
    if complejidad == "A":
        monto_final = monto_final * (1 + RECARGO_ALTA_COMPLEJIDAD)
    return monto_final


# ---------------------------------------------------------------
# ALGORITMOS DE LA TABLA (Incluyendo Algoritmo 4 del TP3)
# ---------------------------------------------------------------
def algoritmo_1(icd10, complejidad, monto_base):
    porcentaje_extra = 0.0
    suma_fija = 0.0
    if monto_base > 60000:
        porcentaje_extra = calcular_porcentaje_normal(icd10, complejidad,
                                                      monto_base)
    if complejidad == "A" and obtener_letra(icd10) != "U":
        suma_fija = monto_base / 2
    return monto_base + porcentaje_extra + suma_fija


def algoritmo_2(icd10, complejidad, monto_base):
    letra = obtener_letra(icd10)
    if "A" <= letra <= "P":
        porcentaje_extra = calcular_porcentaje_normal(icd10, complejidad,
                                                      monto_base)
    elif complejidad == "A":
        porcentaje_extra = calcular_porcentaje_normal(icd10, complejidad,
                                                      monto_base, 2)
    else:
        porcentaje_extra = monto_base * 0.15
    return monto_base + porcentaje_extra


def algoritmo_3(icd10, complejidad, monto_base):
    letra = obtener_letra(icd10)
    monto_extra = 0.0
    if complejidad == "A":
        monto_extra = monto_base * 0.30

    if "A" <= letra <= "L":
        monto_extra += 20000
    elif "M" <= letra <= "P":
        monto_extra += 15000 + 5000 * obtener_bloque(icd10)
    else:
        monto_extra += monto_base * 0.10

    if monto_extra > 60000:
        monto_extra = 60000
    return monto_base + monto_extra


def algoritmo_4(icd10, complejidad, monto_base):
    bloque = obtener_bloque(icd10)
    numero_enfermedad = obtener_decimal(icd10)

    if (bloque % 2) == (numero_enfermedad % 2):
        monto_extra = monto_base * 0.10
    else:
        monto_extra = monto_base * 0.05

    if complejidad == "A":
        monto_extra += 13000

    if monto_extra > 15000:
        monto_extra = 15000

    return monto_base + monto_extra


def calcular_monto_final(id_algoritmo, icd10, complejidad, monto_base):
    if id_algoritmo == 1:
        return algoritmo_1(icd10, complejidad, monto_base)
    elif id_algoritmo == 2:
        return algoritmo_2(icd10, complejidad, monto_base)
    elif id_algoritmo == 3:
        return algoritmo_3(icd10, complejidad, monto_base)
    elif id_algoritmo == 4:
        return algoritmo_4(icd10, complejidad, monto_base)
    else:
        return calculo_normal(icd10, complejidad, monto_base)