def validar_id_pedido(id_pedido):
    return len(id_pedido) ==5 and id_pedido[0].isalpha() and id_pedido[1].isdigit()

def cadastrar_pedido():
    print("\n--- CADASTRO DO PEDIDO ---\n")

    id_pedido = input("ID do pedido: ")#AUTORIZAÇÃO DO ID
    while not validar_id_pedido(id_pedido):
        print("ID do pedido esta invalido. Tente novamente!!")
        id_pedido = input("ID do pedido: ")

    nome_cliente = input("Digite o nome do cliente: ")
    while not nome_cliente.replace(" ", "").isalpha():
        print("Nome inválido! Digite apenas letras.")
        nome_cliente = input("Digite o nome do cliente: ") 

    endereco = input("Digite o enderço da entrega: ")

    prioridade = input("Digite a prioridade do seu pedido (NORMAL/ALTA):").upper()
    while prioridade not in ["ALTA", "NORMAL"]:
        print("Propriedade invalida. Digite se é de prioridade (NORMAL/ALTA)")
        prioridade = input("Digite a prioridade do seu pedido (NORMAL/ALTA):").upper()

    descricao_pedido = str(input("Faça a descrição do pedido: "))
    while len(descricao_pedido) < 5:
        print("Escreva a descrição do pedido realizado!")
        descricao_pedido = str(input("Faça a descrição do pedido: "))

    status_opcoes = ["Pendente", "Em Rota", "Entregue", "Cancelado"]
    print("Status disponíveis: Pendente, Em Rota, Entregue, Cancelado")
    status = input("Digite o status do pedido: ").title().strip()
    while status not in status_opcoes:
        print("Status invalido!! Escoleha entre: Pendente, Em Rota, Entregue, Cancelado .")
        status = input("Digite o status do pedido: ").title().strip()

    id_entregador = input("Digite o ID do entregador: ")
    while len(id_entregador) != 4 or not id_entregador.isdigit():
        print("ID do entregador esta incorreto!! Tente novamente.")
        id_entregador = input("Digite o ID do entregador: ")

    print("\n=== Pedido Cadastrado com Sucesso! ===")
    print(f"ID do Pedido:     {id_pedido}")
    print(f"Cliente:          {nome_cliente}")
    print(f"Endereço:         {endereco}")
    print(f"Prioridade:       {prioridade}")
    print(f"Descrição:        {descricao_pedido}")
    print(f"Status:           {status}")
    print(f"ID do Entregador: {id_entregador}")
