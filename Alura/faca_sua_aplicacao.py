import os

restaurantes = [{"nome" : "praca" , "categoria" : "japonesa" , "ativo":False},
                {"nome" : "pizza suprema" , "categoria" : "pizza" , "ativo":True},
                {"nome" : "cantina" , "categoria" : "italiana" , "ativo":False}] 
def exibir_nome_do_programa():
    nome =("sabor express")
    print(nome)
def exibir_opcoes():
    print ("1.Cadastrar restaurante")
    print("2.Listar restaurantes")
    print("3.Ativar restaurante")
    print("4.Sair\n")
def finalizar_app ():
    exibir_subtitulo("finalizando o app")
def voltar_ao_menu_principal():
    input("digite uma tecla para voltar ao menu principal")
    main()
def opcao_invalida():
    print("opcao inválida\n")
    voltar_ao_menu_principal()
def exibir_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()
def cadastrar_novo_restaurante():
    exibir_subtitulo("cadastro de novos restaurantes")
    nome_do_restaurante = input("digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"o restaurante {nome_do_restaurante} foi cadastrado com sucesso")
    voltar_ao_menu_principal()
def listar_restaurantes():
    exibir_subtitulo("listando todos os restaurantes")
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f" - {nome_restaurante} | {categoria} | {ativo}")
    voltar_ao_menu_principal()
def alternar_estado_do_restaurante():
    exibir_subtitulo("alternando estado do restaurante")
    nome_restaurante = input("digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurantes["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"o restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"o restaurante {nome_restaurante} foi desativado com sucesso"  
            print(mensagem)
    if not restaurante_encontrado:
        print("o restaurante nao foi encontrado")

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("escolha uma opcao: "))
        if opcao_escolhida == 1:
           cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
def main():
    os.system("clear")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
if __name__ == '__main__':
    main()
    