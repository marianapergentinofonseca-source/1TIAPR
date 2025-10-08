#Verificar se é Identidade: Crie uma matriz 3x3 e verifique se ela é uma matriz identidade.

matriz = [[0, 1, 1],
          [0, 0, 0],
          [0, 1, 0]
          ]

if matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2]:
    print("a matriz é identidade")

else:
    print("a matriz nao é identidade")