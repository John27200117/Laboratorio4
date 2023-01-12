import numpy as np

def esSimetrica(matriz,orden):
    simetrica = True
    for i in range(orden):
        for j in range(orden):
            if (matriz[i][j] != matriz[j][i]):
                simetrica = False
    return simetrica

def resultado():
    matriz = [[1,0,1],[0,1,1],[1,1,1]]
    respuesta = esSimetrica(matriz,len(matriz))
    if (respuesta == True):
        print("La matriz es simetrica")
    else:
        print("La matriz NO es simetrica")

resultado()
