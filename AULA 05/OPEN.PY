#Abri um arquivo para escrita

with open("arquivo.txt","w") as file:
    file.write("Olá mundo")

# abrir um arquivo para leitura e escrita
with open("arquivo.txt", "r+") as file:
    conteudo = file.read()
    file.write("\nAdicionando mais conteudo")

#abrir um arquivo para anexo
with open("arquivo.txt","a") as file:
    file.write("\nMais uma linha no final do arquivo")

