# 2. Par ou ímpar
# Receba um número inteiro e verifique se ele é par ou ímpar.

numero = int(input("digite aqui um numero inteiro: "))
if numero %2 == 0:
    print(f"o numero {numero} é par")
else:
    print(f"o numero {numero} é impar")