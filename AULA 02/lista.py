lista_mercado = []
lista_mercado.append("uva")
lista_mercado.append("limao")
lista_mercado.append("maracuja")
lista_mercado.append("banana")
lista_mercado.append("laranja")
lista_mercado.append("maca")
lista_mercado.insert(1,"banana")
lista_mercado.append("maca")

lista_mercado.remove("maca")
lista_mercado.pop(1)
#pop - remove o item (de acordo com o numero da posicao)
#lista_mercado.clear() - limpa a lista
#count - contar
#sort - colocar em ordem (alfabetica ou numerica)


lista_mercado.append(input("digite aqui o item da sua lista: "))
lista_mercado.sort()
print(lista_mercado[4])
