#Contagem de Vogais: Crie uma função que recebe uma
#string e conta quantas vogais (a, e, i, o, u) ela possui. A
#função deve retornar o número de vogais.



frase = input("digite aqui a sua frase: ")
vogais = "aeiouAEIOU"

def vogais_frase(texto):
    contador = 0 
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

resultado = vogais_frase(frase)
print(f"a quantidade de vogais é {resultado}")