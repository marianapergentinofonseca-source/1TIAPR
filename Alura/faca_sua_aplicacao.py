
import os
def exibir_nome_do_programa():
    nome =("sabor express")
    print(nome)
def exibir_opcoes():
    print ("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")
def finalizar_app ():
    os.system("clear")
    print("finalizando o app")
def escolher_opcoes():
    opcao_escolhida = int(input("escolha uma opcao: "))

    if opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
            print("Listar restaurantes")
    elif opcao_escolhida == 3:
            print("Ativar restaurante")
    else:
         finalizar_app()
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
if __name__ == '__main__':
    main()
    