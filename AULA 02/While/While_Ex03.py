import random

tentativas = 3
numero = random.randint(1,10)

while tentativas > 0:
    palpite = int(input("digite um numero entre 1 e 10"))
    if palpite == numero:
        print("Parabens! Voce acertou")
