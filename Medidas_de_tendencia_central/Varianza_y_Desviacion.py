#Libreria Numpy para analisis de datos
import numpy
import random

if __name__ == "__main__":
    
    X = [random.randint(1, 21) for i in range(20)]
    resultado = numpy.std(X)
    resultado2 = numpy.var(X)
    print(X)
    print(f'La desviación es: {resultado}')
    print(f'La varianza es: {resultado2}')

