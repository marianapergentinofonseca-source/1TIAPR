from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# =========================
# CONEXÃO COM O MONGODB
# =========================
def conectar_mongo():
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        cliente.admin.command("ping")  # testa a conexão
        print("Conectado ao MongoDB com sucesso!")
        return cliente
    except ConnectionFailure:
        print("Erro: não foi possível conectar ao MongoDB.")
        return None


# =========================
# FUNÇÕES DO SISTEMA
# =========================
def inserir_usuario(colecao):
    nome = input("Digite o nome: ").strip()
    idade = input("Digite a idade: ").strip()
    email = input("Digite o email: ").strip()

    if not nome or not idade or not email:
        print("Todos os campos são obrigatórios.")
        return

    if not idade.isdigit():
        print("A idade deve ser um número.")
        return

    usuario = {
        "nome": nome,
        "idade": int(idade),
        "email": email
    }

    resultado = colecao.insert_one(usuario)
    print(f"Usuário cadastrado com sucesso! ID: {resultado.inserted_id}")


def listar_usuarios(colecao):
    usuarios = colecao.find()

    print("\n--- USUÁRIOS CADASTRADOS ---")
    encontrou = False
    for usuario in usuarios:
        encontrou = True
        print(f"ID: {usuario['_id']}")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Email: {usuario['email']}")
        print("-" * 30)

    if not encontrou:
        print("Nenhum usuário cadastrado.")


def buscar_usuario_por_nome(colecao):
    nome = input("Digite o nome para buscar: ").strip()

    resultados = colecao.find({"nome": {"$regex": nome, "$options": "i"}})

    print("\n--- RESULTADOS DA BUSCA ---")
    encontrou = False
    for usuario in resultados:
        encontrou = True
        print(f"ID: {usuario['_id']}")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Email: {usuario['email']}")
        print("-" * 30)

    if not encontrou:
        print("Nenhum usuário encontrado.")


def menu():
    print("\n===== SISTEMA DE CADASTRO =====")
    print("1 - Inserir usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário por nome")
    print("4 - Sair")


def main():
    cliente = conectar_mongo()
    if cliente is None:
        return

    banco = cliente["cadastro_db"]
    colecao = banco["usuarios"]

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            inserir_usuario(colecao)
        elif opcao == "2":
            listar_usuarios(colecao)
        elif opcao == "3":
            buscar_usuario_por_nome(colecao)
        elif opcao == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    cliente.close()


if __name__ == "__main__":
    main()