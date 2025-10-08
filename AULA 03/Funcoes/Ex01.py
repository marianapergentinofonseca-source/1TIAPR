# Calculadora Simples: Crie funções para realizar as operações básicas de
#  uma calculadora (adição,subtração, multiplicação, divisão). A função deve
#receber dois números e retornar o resultado da operação.




def conta():
    num1 = int(input("digite aqui um numero: "))
    num2 = int(input("digite aqui um outro numero: "))
    operacao = input("digite aqui a operacao que voce deseja realizar(+, - * ou /): ")

    if operacao == "+":
        resultado_soma = num1 + num1
        print (f"o resultado da soma é {resultado_soma}")

    if operacao == "-":
        resultado_sub = num1 - num2
        print(f"o resultado da subtracao é {resultado_sub}")
    
    if operacao == "*":
        resultado_multi = num1 * num2
        print(f"o resultado da multiplicacao é {resultado_multi}")

    if operacao == "/":
        resultado_divi = num1*num2
        print(f"o resultado da divisao é {resultado_multi}")
    else:
        print("digite um numero ou operacao valida")
    


conta()