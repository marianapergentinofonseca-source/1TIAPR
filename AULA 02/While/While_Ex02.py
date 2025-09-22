numero = int(input("digite aqui um numero par: ")) 
while numero %2 != 0:
        print("digite outro numero")
        numero = int(input("digite aqui um numero par: "))
print(f"o numero {numero} é par")