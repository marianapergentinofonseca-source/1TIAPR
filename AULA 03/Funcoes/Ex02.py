#Verificar Número Primo: Crie uma função que recebe
#um número e verifica se ele é primo. A função deve
#retornar True se o número for primo e False caso
#contrário.

def numero_primo():
    numero = int(input("digite aqui um numero maior ou igual a 1: "))

    if numero % numero == 0 and numero % 1==0:
        print(f"o numero {numero} é primo ")
    else:
        print("o numero nao é primo")

numero_primo()
        