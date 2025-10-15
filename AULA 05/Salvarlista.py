lista = ["maca", "banana", "uva", "abacate", "abacaxi"]
with open("frutas.txt", "w") as arquivo:
        for fruta in lista:
                arquivo.write(fruta + "\n")