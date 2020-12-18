import random
import collections

PALOS = ['Espada', 'Corazon', 'Diamante', 'Trevol']
VALORES = ['AS', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))

    return barajas
def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    
    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = [] 

    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0

    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter =  dict(collections.Counter(valores))
        
        for val in counter.values():
            if val == 2:
                pares += 1
                break

        tercia = 0

        for val1 in counter.values():
            if val1 == 3:
                tercia += 1
                break

        corrida = 0

        for val2 in counter.values():
            if val2 == 5:
                corrida += 1
                break
        
    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} cartas es {probabilidad_par}')

    probabilidad_tercia = tercia / intentos
    print(f'La probabilidad de obtener una tercia en una mano de {tamano_mano} cartas es {probabilidad_tercia}')

    probabilidad_corrida = corrida / intentos
    print(f'La probabilidad de obtener una corrida en una mano de {tamano_mano} cartas es {probabilidad_corrida}')

if __name__ == "__main__":

    tamano_mano = int(input('De cuatas cartas sera la mano: '))
    intentos = int(input('Cuantos intentos vamos a realizar: '))

    barajas = crear_baraja()
    mano = obtener_mano(barajas, 5)
    print(f'Tus cartas en la mano son: {mano}')

    main(tamano_mano, intentos)