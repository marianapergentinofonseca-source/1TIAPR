import os 
from funcoes import *


def exibir_nome_do_programa():
    nome =("Totem FlexMedia")
    print(nome)

def exibir_opcoes():
    print ("1.Cadastrar informacoes")
    print("2.Listar informacoes dos totens cadastrados")
    print("3. Pesquisar totens por tipo de categoria")
    print("0.Sair\n")

def voltar_ao_menu_principal():
    input("digite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    print("opcao inválida\n")
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("escolha uma opcao: "))
        if opcao_escolhida == 1:
           cadastrar_informacoes()
        elif opcao_escolhida == 2:
            listar_totens_cadastrados()
        elif opcao_escolhida == 3:
            pesquisa_categoria()
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