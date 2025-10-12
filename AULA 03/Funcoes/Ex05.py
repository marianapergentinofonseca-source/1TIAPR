#Fatorial: Crie uma função que recebe um número e
#retorna o seu fatorial. O fatorial de um número n é o
#produto de todos os números inteiros positivos
#menores ou iguais a n

def fatorial(num):
    if num<0:
        return "Erro: numero negativo"
    elif num ==0 or num ==1:
        return 1
    else:
        resultado = 1
        for i in range(2, num +1):
            resultado *=1
        return resultado

numero = 5
fatorial_numero = fatorial(numero)
print(f"o fatorial de {numero} é {fatorial_numero}")