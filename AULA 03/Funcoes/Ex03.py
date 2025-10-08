#Média de uma Lista: Crie uma função que recebe uma
#lista de números e retorna a média dos elementos.

lista_numero = [3, 1, 5, 7]

def media(lista_numero):
    return sum(lista_numero)/len(lista_numero)

resultado = media(lista_numero)

print(resultado)