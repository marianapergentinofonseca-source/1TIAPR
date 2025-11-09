
import os

lista_dicionarios = [{"titulo" : "totem para zoologico" , "tipo" : "cultural" , "descricao" : "programa para ser utilziado em zoologico", "ativo":True}, 
{"titulo" : "totem para escola", "tipo" : "educativo" , "descricao" : "programa para ser utilizado em escolas para tirar os alunos do celular", "ativo":True},
{"titulo" : "totem para parque de diversao", "tipo" : "lazer" , "descricao" : "programa para ser utilizado em escolas para tirar os alunos do celular", "ativo":True}]

def voltar_ao_menu_principal():
    from main import voltar_ao_menu_principal as _voltar
    _voltar()

def finalizar_app():
    exibir_subtitulo("finalizando o app")

def exibir_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()

def cadastrar_informacoes():
    exibir_subtitulo("cadastro totem")
    titulo_do_totem = input("digite o titulo do totem que deseja cadastrar: ")
    if not titulo_do_totem.strip():
        print("erro: o titulo do totem não pode estar vazio")
        voltar_ao_menu_principal()
        return True
    elif titulo_do_totem:
        print(f"o titulo do totem {titulo_do_totem} foi cadastrado com sucesso")
    
    while True:
        categoria = input(f"digite o nome da categoria do totem {titulo_do_totem} - escolha entre as opcoes cultural, educativo ou lazer:")
        if categoria == "educativo":
                print (f"o totem {titulo_do_totem} foi cadastrado com sucesso na categoria educativo")
                break
        if categoria == "cultural":
                print (f"o totem {titulo_do_totem} foi cadastrado com sucesso na categoria cultural")
                break
        if categoria == "lazer":
                print (f"o totem {titulo_do_totem} foi cadastrado com sucesso na categoria lazer")
                break
        elif categoria:
            print("digite uma categoria válida")

    dados_do_totem = {"titulo": titulo_do_totem, "tipo": categoria, "ativo": True}
    lista_dicionarios.append(dados_do_totem)
    voltar_ao_menu_principal()

def listar_totens_cadastrados():
    exibir_subtitulo("listando todos os totens cadastrados")
    for totem in lista_dicionarios:
        nome_totem = totem["titulo"]
        categoria = totem ["tipo"]
        ativo = totem ["ativo"]
        print(f" - {nome_totem} | {categoria} | {ativo}")
    voltar_ao_menu_principal() 

def pesquisa_categoria():
    categoria_escolhida = input ("digite a categoria que deseja visualizar (educativo, cultural ou lazer)")
    exibir_subtitulo (f"listando todos os totens cadastrados na categoria {categoria_escolhida}")
    totens_encontrados = []

    for totem in lista_dicionarios:
        if totem["tipo"].lower() == categoria_escolhida.lower():
            totens_encontrados.append(totem["titulo"])

    if totens_encontrados:
        print("\nTotens encontrados:")
        for titulo in totens_encontrados:
            print(f"- {titulo}")
    else:
        print("\nNenhum totem cadastrado nessa categoria ou categoria inválida.")

    voltar_ao_menu_principal()
