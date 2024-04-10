import random

# Crear registro...
class Proyecto:
    def __init__(self, num, tit, dd, mm, year, leng, cant):
        self.numero = num
        self.titulo = tit
        self.dia = dd
        self.mes = mm
        self.anio = year
        self.lenguaje = leng
        self.lineas = cant


def to_string(registro):
    lenguajes = ["Python", "Java", "C++", "Javascript",
                 "Shell", "HTML", "Ruby", "Swift", "C#", "VB", "Go"]
    for i in range(11):
        if registro == i:
            return lenguajes[i]


def write(registro):
    t = ("\nNumero: {:<5} | Titulo: {:<10} | Fecha: {:<2}/{:<2}/{:<4} | Lenguaje: {:<10} | Cantidad de lineas: {}")
    return t.format(registro.numero, registro.titulo, registro.dia, registro.mes, registro.anio, to_string(registro.lenguaje), registro.lineas)


def ver(vec, tamano):
    numero = random.randint(1, tamano + 1)
    while numero in vec:
        numero = random.randint(1, tamano + 1)
    vec.append(numero)
    return numero