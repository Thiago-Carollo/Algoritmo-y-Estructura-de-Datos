import random

salir = True
pedir = True
nombre = input("Ingrese su Nombre: ")
monto = int(input("Ingrese su monto, el cual no puede superar los $100000: $"))
victorias = 0
contadorpartidas = 0
blackjacknatural = 0
perdidamasgrande = 0
mayormonto = 0
sumadeapuestas = 0
mayorracha = 0
victoriascroupier = 0
racha = 0
contbjn = 0

# Funciones


def repartirCartas():
    palo = ("♠Pica♠", "♥Corazon♥", "♦Diamante♦", "♣Trebol♣")
    numero = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
    numero1 = random.choice(numero)
    palo1 = random.choice(palo)
    if numero1 == "J" or numero1 == "Q" or numero1 == "K":
        numero1 = 10
    if numero1 == "A":
        numero1 = 11
    carta1 = str(numero1) + ' ' + palo1
    return numero1


def aS(carta, sumacartas):
    if carta == 11:
        if sumacartas > 21:
            carta = 1
        else:
            carta = 11
    else:
        carta = carta
    return carta


def perdidamayor(perdidamasgrande, apuesta):
    if perdidamasgrande == 0:
        perdidamasgrande = apuesta
    elif perdidamasgrande < apuesta:
        perdidamasgrande = apuesta

    return perdidamasgrande


def montomayor(mayormonto, monto):
    if mayormonto == 0:
        mayormonto = monto
    elif mayormonto < monto:
        mayormonto = monto

    return mayormonto


def rachamaslarga(mayorracha, victoriascroupier):
    if victoriascroupier >= 2 and victoriascroupier > mayorracha:
        mayorracha = victoriascroupier
    return mayorracha


def sumabjn(contbjn):
    if contcroupier == 2 and sumacroupier == 21 and contjugador == 2 and sumajugador == 21:
        contbjn += 1

# Ciclo


while True:
    if monto > 100000 or monto < 1:
        monto = int(
            input("Error con el ingreso del monto, por favor vuelva a intentarlo: $"))
    else:
        break
while salir:
    print("""1- Apostar \n2- Jugar una Mano \n3- Salir""")
    opcion = int(input("Ingrese una opcion: "))

    if (opcion == 1):
        monto_sumar = int(
            input("Ingrese la cantidad de dinero que quiere sumar a su monto: $"))
        while True:
            if monto_sumar < 1:
                monto_sumar = int(
                    input("Error con el ingreso del dinero a sumar, por favor vuelva a ingresarlo: $"))
            else:
                break
        monto += monto_sumar
        mayormonto = montomayor(mayormonto, monto)
    elif (opcion == 2):
        apuesta = int(input("ingrese el monto a apostar: $"))
        print("Usted a apostasdo $", apuesta,
              ", y su nuevo monto total es de $", monto-apuesta)
        mayormonto = montomayor(mayormonto, monto)
        if apuesta % 5 == 0 and apuesta <= monto:

            sumadeapuestas += apuesta

            # Jugador
            contadorpartidas += 1
            cartajugador1 = repartirCartas()
            cartajugador2 = repartirCartas()
            contjugador = 2
            print("Su primera carta es: ", cartajugador1)
            print("Su segunda carta es: ", cartajugador2)
            sumacartasjugador = cartajugador1 + cartajugador2
            cartajugador1 = aS(cartajugador1, sumacartasjugador)
            cartajugador2 = aS(cartajugador2, sumacartasjugador)
            sumajugador = cartajugador1 + cartajugador2
            cartajugadorlista = [cartajugador1, cartajugador2]

            parar = int(input("Deasea pedir otra carta: 1-Si 2-No: "))
            while parar == 1 and sumajugador <= 20:
                cartajugador = repartirCartas()
                sumacartasjugador += cartajugador
                if cartajugador == 11 and sumacartasjugador >= 21:
                    cartajugador = aS(cartajugador, sumacartasjugador)
                cartajugadorlista.append(cartajugador)
                contjugador += 1
                sumajugador += cartajugador
                print("Su nueva carta agregada es: ", cartajugador)
                parar = int(input("Deasea pedir otra carta: 1-Si 2-No: "))

            # Croupier
            cartacroupier1 = repartirCartas()
            contcroupier = 1
            sumacroupier = cartacroupier1
            sumacartascroupier = cartacroupier1
            cartacroupierlista = [cartacroupier1]
            while True:
                if sumacroupier <= 16:
                    cartacroupier = repartirCartas()
                    sumacartascroupier += cartacroupier
                    if cartacroupier == 11 and sumacartascroupier >= 21:
                        cartacroupier = aS(cartacroupier, sumacartascroupier)
                    cartacroupierlista.append(cartacroupier)
                    contcroupier += 1
                    sumacroupier += cartacroupier
                else:
                    break
                print

            # Mostrar Cartas

            print("Cartas del Jugador: ")
            for cartas in cartajugadorlista:
                print(cartas)
            print("Cartas del Croupier: ")
            for cartas in cartacroupierlista:
                print(cartas)

            # Quien Gana

            if sumajugador <= 21 and (sumacroupier > 21 or (sumacroupier < sumajugador)):
                print("Usted ha ganado con una suma de: ",
                      sumajugador, ". Recibira el doble de su apuesta")
                victorias += 1
                monto = apuesta * 2
                victoriascroupier = 0
                print("Su monto se actualizo: $", monto)
                sumabjn(contbjn)

            elif sumacroupier <= 21 and (sumajugador > 21 or (sumajugador < sumacroupier)):
                print("Usted ha perdido, le ha ganado el Crupier con la suma de ", sumacroupier,
                      ". Ha perdido su apuesta")
                monto -= apuesta
                victoriascroupier += 1
                print("Su monto se actualizo: $", monto)
                perdidamasgrande = perdidamayor(perdidamasgrande, apuesta)
                sumabjn(contbjn)

            elif sumajugador > 21 and sumacroupier > 21:
                print("Usted ha perdido ya que se ha pasado. Ha perdido su apuesta")
                monto -= apuesta
                victoriascroupier = 0
                print("Su monto se actualizo: $", monto)
                perdidamasgrande = perdidamayor(perdidamasgrande, apuesta)
                sumabjn(contbjn)

            elif contjugador == 2 and contjugador < contcroupier and sumajugador == 21 and sumacroupier == 21:
                print(
                    "Usted ha ganado, ya que su Blackjack es natural y el del croupier no. Recibira el doble de su apuesta")
                monto = apuesta * 2
                victoriascroupier = 0
                print("Su monto se actualizo: $", monto)
                victorias += 1
                blackjacknatural += 1
                sumabjn(contbjn)

            elif contjugador > contcroupier and contcroupier == 2 and sumajugador == 21 and sumacroupier == 21:
                print(
                    "Usted ha perdido, ya que su Blackjack no es natural, pero el del croupier si. Ha perdido su apuesta")
                monto -= apuesta
                victoriascroupier += 1
                print("Su monto se actualizo: $", monto)
                blackjacknatural += 1
                perdidamasgrande = perdidamayor(perdidamasgrande, apuesta)
                sumabjn(contbjn)

            elif sumajugador == sumacroupier and sumajugador <= 21 and sumacroupier <= 21:
                print("Usted y el croupier han empatado. Se le devolvera la apuesta")
                print("Su monto no se actualizo: $", monto)
                sumabjn(contbjn)

            mayorracha = rachamaslarga(mayorracha, victoriascroupier)

        else:
            print("No se puede apostar, ya que no tiene el suficiente dinero")

    elif (opcion == 3):

        # Porcentaje de victorias del jugador
        porcentajevictorias = (victorias * 100) / contadorpartidas
        print("Porcentaje de victorias del jugador: %", porcentajevictorias)

        # La racha de vitorias mas larga del croupier
        print("La mayor racha del croupier es de:", mayorracha)

        # Cantidad de blackjack natural
        print("Cantidad de blackjack natural:", contbjn)

        # El monto maximo que llego a tener el jugador en el pozo
        print("El monto maximo que llego a tener el jugador en el pozo: $", mayormonto)

        # El monto promedio del que disputo el jugador para realizar apuestas
        promedioapuestas = sumadeapuestas / contadorpartidas
        print("Monto promedio del que disputo el jugador para realizar apuestas :", promedioapuestas)

        # La perdida mas grande que sufrio el jugador(si hubo alguna)
        print("La perdida mas grande que sufrio el jugador :", perdidamasgrande)
        break
