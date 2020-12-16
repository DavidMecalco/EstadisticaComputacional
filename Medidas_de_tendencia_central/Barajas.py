
PALOS = ['Espada', 'Corazon', 'Diamante', 'Trevol']
VALORES = ['AS', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))

    return barajas

if __name__ == "__main__":
    barajas = crear_baraja()
    print(barajas)
