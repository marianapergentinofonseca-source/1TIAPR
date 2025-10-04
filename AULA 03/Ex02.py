#Crie uma matriz 2x2 e um escalar. Multiplique a matriz pelo escalar

Matriz = [[10, 11],
          [13, 14]
          ]

Escalar = 3

Matriz_2= [[0, 0],
           [0, 0]
           ]

for i in range(2):
    for j in range(2):
        Matriz_2[i][j] = Matriz[i][j] * Escalar

print(Matriz_2)