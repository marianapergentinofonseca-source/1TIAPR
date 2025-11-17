#def calcular_media_horas(lista_colaboradores): """Retorna a média de horas trabalhadas
#def maior_estresse (lista_colaboradores): """Retorna o nome do colaborador com maior nível de estresse"
#def colaboradores_produtivos(lista_colaboradores): """Retorna os nomes dos que realizaram 5 ou mais tarefas"
#def alerta_equilibrio(lista_colaboradores):"Retorna os colaboradores com estresse >= 4 e pausas <= 1""

from Workbalanceia import lista_dicionarios

def calcular_media_horas():
    soma_horas = 0

    for colaborador in lista_dicionarios:
        horas = colaborador["horas trabalhadas semanalmente"]
        soma_horas += horas   # soma das horas

    media = soma_horas / len(lista_dicionarios)
    return media
media = calcular_media_horas()
print(f"a média de horas de {media}")

def maior_estresse():
    num_maior_estresse = -1
    colab_maior_estresse = None
    for colaborador in lista_dicionarios:
        nivel = colaborador["nível de estresse"]
        if nivel > num_maior_estresse:
            num_maior_estresse = nivel
            colab_maior_estresse = colaborador
    
    return colab_maior_estresse, num_maior_estresse

colaborador, nivel = maior_estresse()
print(f"O colaborador com maior nível de estresse é {colaborador['nome_colaborador']} com nível {nivel}.")

def listar_colaboradores_com_5_ou_mais_tarefas():
    print("\nColaboradores com 5 ou mais tarefas:\n")
    encontrou = False

    for colaborador in lista_dicionarios:
        atividades_texto = colaborador["atividades"]

        # separa as atividades pela vírgula
        lista_atividades = [atividade.strip() for atividade in atividades_texto.split(",")]

        # conta quantas atividades existem
        quantidade = len(lista_atividades)

        if quantidade >= 5:
            encontrou = True
            print(f"- {colaborador['nome_colaborador']} realizou {quantidade} tarefas")

    if not encontrou:
        print("Nenhum colaborador realizou 5 ou mais tarefas.")
listar_colaboradores_com_5_ou_mais_tarefas()

def alerta_equilibrio():
    print("n/listando colaboradores com estresse >=4 ou pausas <=1")
    colab_estressados = []

    for colaborador in lista_dicionarios:
        estresse = colaborador["nível de estresse"]
        pausas = colaborador["pausas"]
        if estresse >= 4 and pausas <= 1:
            colab_estressados.append(colaborador["nome_colaborador"])

    if len(colab_estressados) > 0:
        print(f"os colaboradores com alerta de equilibrio sao {colab_estressados}")
    elif len(colab_estressados) == 0:
        print("nao temos colaboradores em alerta de estresse")
alerta_equilibrio()