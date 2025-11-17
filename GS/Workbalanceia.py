import os 

lista_dicionarios =[{"nome_colaborador" : "Mariana Fonseca" , "departamento" : "desenvolvimento de solucoes sustentaveis" , "horas trabalhadas semanalmente" : 100, "pausas": 1, "nível de estresse" : 5 , "atividades" : "criacao de 5 programas, debig dos erros, testes, reuniao com cleinte, reuniao interna do time"}, 
{"nome_colaborador" : "Alexandre" , "departamento" : "vendas" , "horas trabalhadas semanalmente" : 50, "pausas": 1 , "nível de estresse" : 5 , "atividades" : "visita a clientes, envio de propostas, almoco com cliente, validacoa com desenvolvedor, reunioes internas, reuniao de alinhamento com time"},
{"nome_colaborador" : "Julia" , "departamento" : "educacao" , "horas trabalhadas semanalmente" : 14, "pausas": 1 , "nível de estresse" : 5 , "atividades" : "aulas, estudo de materiais para execucao das aulas"}]

def exibir_nome_do_programa():
    nome =("Registro de colaboradores - SynWork")
    print(nome)

def listar_colaboradores():
    exibir_subtitulo("listando todos os colaboradores cadastrados")
    for colaborador in lista_dicionarios:
        nome = colaborador ["nome_colaborador"]
        departamento = colaborador ["departamento"]
        horas = colaborador ["horas trabalhadas"]
        print(f" - {nome} | {departamento} | {horas}")
    voltar_ao_menu_principal() 

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("escolha uma opcao: "))
        if opcao_escolhida == 1:
           cadastrar_informacoes_colab()
        
        if opcao_escolhida ==2:
            listar_colaboradores()
        else:
            opcao_invalida()
            return False
    except ValueError:
        print("Por favor, digite um número válido.")
        voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()

def exibir_opcoes():
    print ("1.Cadastrar informacoes dos colaboradores")
    print ("2.Exibir informacoes dos colaboradores")
    print("0.Sair\n")

def voltar_ao_menu_principal(): 
    input("digite uma tecla para voltar ao menu principal: ")
    main()

def cadastrar_informacoes_colab():
    exibir_subtitulo("cadastrar informacoes do colaborador")
    nome_colaborador = input("digite o nome do colaborador: ")
    if not nome_colaborador.strip():
        print("ERRO: o nome do colaborador nao pode estar vazio")
    elif nome_colaborador:
        print(f"o colaborador {nome_colaborador} foi cadastrado com sucesso")
    
    departamento = input("digite o departamento do colaborador: ")
    if not departamento.strip():
        print("ERRO: o departamento nao pode estar vazio")
    elif nome_colaborador:
        print(f"o colaborador {nome_colaborador} foi cadastrado com sucesso no departamento: {departamento}")

#entrando em horas trabalhadas - adidionando verificacoes se esta sendo feita a entreada de numeros 
    while True:
        horas_trabalhadas = input("digite a quantidade de horas trabalhadas para o colaborador: ")
        if not horas_trabalhadas.isdigit():
            print("ERRO: a quantidade de horas nao pode ser em texto ou estar vazio")
            continue
        horas_trabalhadas = int(horas_trabalhadas)
        print(f"foram cadastradas {horas_trabalhadas} pra o colaborador {nome_colaborador}")
        break

#entrando em pausas - adidionando verificacoes se esta sendo feita a entreada de numeros 
    while True:
        pausas = input("digite a quantidade (em número) de pausas realizadas pelo o colaborador: ")
        if not pausas.isdigit():
            print("ERRO: a quantidade de pausas nao pode ser em texto ou estar vazio")
            continue

        print(f"foram cadastradas {pausas} pausas para o colaborador {nome_colaborador}")
        break
#entrando em nivel de estressa - adidionando verificacoes se esta sendo feita a entreada de numeros apenas de 1 a 5
    while True:
            nivel_estresse = input("digite o nível de estresse percebido (de 1 a 5): ")          
            if not nivel_estresse.isdigit():
                print("por favor digite um numero de 1 a 5, textos nao sao permitidos")
                continue   
            if int(nivel_estresse) < 1 or int(nivel_estresse) > 5:
                print("por favor digite um numero de 1 a 5")
                continue  
            print("nivel de estresse cadastrado com sucesso")
            break  
        
    atividades = input("liste as atividades realizadas pelo colaborador: ")
    if not atividades.strip():
            print("ERRO: as atividades nao podem estar vazias")
    elif nome_colaborador:
            print(f"as atividades cadastradas pelo colaborador foram {atividades}")
    
    dados_colaborador = {"nome do colaborador": nome_colaborador,"departamento": departamento,"horas trabalhadas": horas_trabalhadas,"pausa": pausas,"nível de estresse": nivel_estresse,"atividades": atividades}
    lista_dicionarios.append(dados_colaborador)

    lista_dicionarios.append(dados_colaborador)
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