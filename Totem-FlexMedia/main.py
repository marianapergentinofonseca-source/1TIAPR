import os 

lista_dicionarios = [{"titulo" : "totem para zoologico" , "tipo" : "educativo" , "descricao" : "programa para ser utilziado em zoologico", "ativo":True}, 
{"titulo" : "totem para farmácia", "tipo" : "comercial" , "descricao" : "programa para ser utilizado em farmacias para orienctacao de produtos", "ativo":True}]
def exibir_nome_do_programa():
    nome =("Totem FlexMedia")
    print(nome)
def exibir_opcoes():
    print ("1.Cadastrar informacoes")
    print("2.Listar informacoes dos totens cadastrados")
    print("0.Sair\n")
def finalizar_app():
    exibir_subtitulo("finalizando o app")
def voltar_ao_menu_principal():
    input("digite uma tecla para voltar ao menu principal: ")
    main()
def opcao_invalida():
    print("opcao inválida\n")
    voltar_ao_menu_principal()
def exibir_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()
def cadastrar_informacoes():
    exibir_subtitulo("cadastro totem")
    titulo_do_totem = input("digite o titulo do totem que deseja cadastrar: ")
    categoria = input(f"digite o nome da categoria do totem {titulo_do_totem}: ")
    dados_do_totem = {"titulo": titulo_do_totem, "tipo": categoria, "ativo": True}
    lista_dicionarios.append(dados_do_totem)
    print(f"o totem {titulo_do_totem} foi cadastrado com sucesso")
    voltar_ao_menu_principal()
def listar_totens_cadastrados():
    exibir_subtitulo("listando todos os totens cadastrados")
    for totem in lista_dicionarios:
        nome_totem = totem["titulo"]
        categoria = totem ["tipo"]
        ativo = totem ["ativo"]
        print(f" - {nome_totem} | {categoria} | {ativo}")
    voltar_ao_menu_principal() 
def escolher_opcoes():
    try:
        opcao_escolhida = int(input("escolha uma opcao: "))
        if opcao_escolhida == 1:
           cadastrar_informacoes()
        elif opcao_escolhida == 2:
            listar_totens_cadastrados()
        elif opcao_escolhida ==0:
            finalizar_app()
            return False
        else:
            opcao_invalida()
            return False
    except ValueError:
        print("Por favor, digite um número válido.")
        voltar_ao_menu_principal()
def main():
    while True:
        os.system("clear")
        exibir_nome_do_programa()
        exibir_opcoes()
        if not escolher_opcoes():
            break    
if __name__ == '__main__':
    main()