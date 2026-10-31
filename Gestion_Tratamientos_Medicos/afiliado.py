class Afiliado:
    def __init__(self, dni, cod_obra_social, nivel_cobertura, tope):
        self.dni = dni
        self.cod_obra_social = cod_obra_social
        self.nivel_cobertura = nivel_cobertura
        self.tope = tope

    def __str__(self):
        return (f"DNI: {self.dni} | Obra Social: {self.cod_obra_social} | "
                f"Nivel: {self.nivel_cobertura} | Tope: {self.tope}")