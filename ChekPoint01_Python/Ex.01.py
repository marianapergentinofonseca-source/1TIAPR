# 1. Número positivo ou negativo
# Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.

numero = int(input("digite aqui um numero: "))
if numero >0:
    print(f"o numero {numero} é positivo") 
if numero<0:
    print(f"o numero {numero} é negativo")
else:
    print(f"o numero {numero} é zero")