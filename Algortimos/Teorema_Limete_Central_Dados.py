import random
import numpy
#from bokeh import figure, figure, output_file, showos.system('cls')
    
    

def tirar_dados(intentos):
    caras_dado1 = []
    caras_dado2 = []
    caras_dado1 = random.choice(['1', '2', '3', '4', '5', '6'])
    caras_dado2 = random.choice(['1', '2', '3', '4', '5', '6'])
    for intentos in caras_dado1 in range(6):
        for intentos in caras_dado2 in range(6):
            resultado_de_dados = [caras_dado1, caras_dado2]
            print(resultado_de_dados)
    return resultado_de_dados

if __name__ == "__main__":
    
    intentos = int(input('Cuanas veces quieres tirar los Dados? :'))
    
    tirar_dados(intentos)