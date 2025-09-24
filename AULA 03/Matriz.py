# matriz inicial
matriz = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

# adicionando uma nova linha a matriz
# nova_linha = [10, 11, 12]
# matriz.append(nova_linha)
# print(matriz)

# imprimindo a matriz atualizada 
# for linha in matriz:
#     print(linha)
    

# # adicionando um elemnto 100 a segunda linha da primeira posicao
# matriz[1].insert(0,100) 

# # usando del para remover a segunda linha
# del matriz[1]

# # imprimindo a matriz apos a remocao da segunda linha
# for linha in matriz:
#     print(linha)

# usando "pop" para remover o obter o elemento na terceira coluna da primeira linha 
#  o codigo salva o numero indicado como uma variavel "elemetno"
# elemento = matriz[0].pop(2)
# print("\nelemento removido", elemento)

# print("\n matriz apos a remocao do elemnto")
# for linha in matriz:
#     print(linha)


# Iterar sobre cada linha da matriz
for linha in matriz: 
# iterar sobre cada elemento da linha
    for elemento in linha:
        print(elemento, end=" ")
# imiprimir uma lonha apos cada linha da matriz
    print()

