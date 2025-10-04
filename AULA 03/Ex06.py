# Subtração de Matrizes: Crie duas matrizes 2x2 e calcule a diferença entre elas.

matriz1 = [[10, 11],
           [12, 13]
           ]

matriz2 = [[14, 15],
           [16, 17]
           ]

diferenca = [[0, 0],
             [0, 0]
             ]
for i in range(2):
    for j in range(1):
        diferenca[i][j] = matriz1[i][j] - matriz2[i][j]

print(diferenca)