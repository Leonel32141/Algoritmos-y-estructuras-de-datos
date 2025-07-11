def intercambiar_filas(matriz, f1, f2):
    matriz[f1], matriz[f2] = matriz[f2], matriz[f1]
    return matriz

matriz = [
    [0, 4, 2, 1],
    [5, 0, 3, 2],
    [0, 2, 0, 1],
    [1, 0, 2, 0]
]

print(intercambiar_filas(matriz, 0, 1))
