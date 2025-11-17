
import numpy as np
from Workbalanceia import lista_dicionarios

def gerar_relatorio_workbalance():
    # ----- 1. Vetores NumPy -----
    horas = np.array([colab["horas trabalhadas semanalmente"] for colab in lista_dicionarios], dtype=float)
    estresse = np.array([colab["nível de estresse"] for colab in lista_dicionarios], dtype=float)

    # ----- 2. Métricas principais -----
    media_horas = horas.mean()
    desvio_horas = horas.std()               # desvio padrão (populacional)
    media_estresse = estresse.mean()

    # ----- 3. Colaborador mais estressado -----
    colaborador_mais_estressado = max(
        lista_dicionarios,
        key=lambda c: c["nível de estresse"]
    )["nome_colaborador"]

    # ----- 4. Colaboradores com 5+ tarefas -----
    colaboradores_5_tarefas = []
    for colab in lista_dicionarios:
        atividades_texto = colab["atividades"]
        atividades_lista = [a.strip() for a in atividades_texto.split(",") if a.strip()]
        if len(atividades_lista) >= 5:
            colaboradores_5_tarefas.append(colab["nome_colaborador"])

    # ----- 5. Alerta de equilíbrio -----
    alerta_equilibrio = []
    for colab in lista_dicionarios:
        nivel = colab["nível de estresse"]
        pausas = colab["pausas"]
        if nivel >= 4 and pausas <= 1:
            alerta_equilibrio.append(colab["nome_colaborador"])

    # ----- 6. Impressão do relatório -----
    print("RELATÓRIO WORKBALANCE AI")
    print("-" * 33)
    print(f"Média de horas trabalhadas: {media_horas:.1f}h")
    print(f"Desvio padrão de horas: {desvio_horas:.1f}")
    print(f"Média de estresse: {media_estresse:.1f}")
    print(f"Colaborador mais estressado: {colaborador_mais_estressado}")
    print(f"Colaboradores com 5+ tarefas: {colaboradores_5_tarefas}")
    print(f"Alerta de equilíbrio: {alerta_equilibrio}")

# para testar direto:
if __name__ == "__main__":
    gerar_relatorio_workbalance()
