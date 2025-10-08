# Crie uma matriz 3x2 e calcule sua transposta

matriz = [[10, 11],
          [12, 13],
          [14, 15]
          ]

transposta = [[0, 0,0],
              [0, 0, 0]
              ]


for i in range(3):
    for j in range(2):
        transposta[j][i] = matriz[i][j]
    
print(transposta)